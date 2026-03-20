import os
import json
import torch
from PIL import Image
from tqdm import tqdm
from transformers import AutoModelForCausalLM, AutoProcessor
import traceback

os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"

# ========== 模型加载 ========== 
def load_model_and_processor(model_path):
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
    ).eval()
    processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)
    return model, processor

# ========== 单样本处理函数 ==========
def run_kimi_instruct_prediction(model, processor, image_path: str, question: str) -> str:
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image path not found: {image_path}")

    image = Image.open(image_path).convert("RGB")
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image},
                {"type": "text", "text": question}
            ],
        }
    ]

    text_input = processor.apply_chat_template(
        messages, add_generation_prompt=True, return_tensors="pt"
    )

    inputs = processor(
        images=image,
        text=text_input,
        return_tensors="pt",
        padding=True,
        truncation=True
    ).to(model.device)

    with torch.inference_mode():
        generated_ids = model.generate(**inputs, max_new_tokens=512)

    generated_ids_trimmed = generated_ids[:, inputs.input_ids.shape[1]:]
    response = processor.batch_decode(
        generated_ids_trimmed, skip_special_tokens=True
    )[0]
    return response.strip()

# ========== 批量处理主函数 ==========
def batch_process_json_file(model, processor, input_file, output_file):
    with open(input_file, "r") as f:
        data_list = json.load(f)

    with open(output_file, "w") as f:
        pass

    for idx, sample in enumerate(tqdm(data_list, desc="Kimi推理中", ncols=100)):
        try:
            image_path = sample["images"][0]
            question = sample["messages"][0]["content"]
            label = sample["messages"][1]["content"]

            predict = run_kimi_instruct_prediction(model, processor, image_path, question)

            result = {
                "predict": predict,
                "label": label.strip()
            }

            with open(output_file, "a") as fout:
                fout.write(json.dumps(result, ensure_ascii=False) + "\n")

        except Exception as e:
            print(f"[Error] Sample #{idx} failed: {e}")
            traceback.print_exc()

# ========== 主程序入口 ==========
if __name__ == "__main__":
    input_file = "dataset_path.json"
    
    model_variants = {
        "instruct": "your_instruct_model_path",
        #"thinking": "your_thinking_model_path"
    }

    for name, path in model_variants.items():
        
        print(f"\n🟢 开始运行模型：{name}")
        output_file = f"your_path.jsonl"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        model, processor = load_model_and_processor(path)
        batch_process_json_file(model, processor, input_file, output_file)

    print("\n✅ 所有模型推理完成")


