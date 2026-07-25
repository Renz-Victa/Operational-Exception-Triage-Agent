from llama_cpp import Llama

class LLMClient:
  def __init__(self):
    self.llm = Llama(
      model_path="models/model.gguf",
      n_ctx=4096,
      n_threads=4,
      verbose=False,
    )

  def generate(self, prompt):
    output = self.llm(
      prompt,
      max_tokens=256,
      temperature=0.7,
    )

    return output["choices"][0]["text"]

def main():
  LLMClient()

if __name__ == "__main__":
  main()