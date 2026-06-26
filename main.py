# import streamlit
from agent.agent import agent
from langchain.agents import create_agent

def main():
    question = "how many employees do we have in the company?."

    stream = agent.stream_events(
    {"messages": [{"role": "user", "content": question}]},
    version="v3",
    )
    for kind, item in stream.interleave("messages", "tool_calls"):
        if kind == "messages":
            for token in item.text:
                print(token, end="", flush=True)
        elif kind == "tool_calls":
            print(f"\nTool call: {item.tool_name}({item.input})")
            for delta in item.output_deltas:
                print(delta, end="", flush=True)
            print(f"\nTool result: {item.output}")

    final_state = stream.output


if __name__ == "__main__":
    main()
