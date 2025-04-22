from nearai.agents.environment import Environment

test
def run(env: Environment):
    # Your agent code here
    # Agent 2
    prompt = {"role": "system", "content": "gh-upload-test"}
    result = env.completion([prompt] + env.list_messages())
    env.add_reply(result)
    env.request_user_input()

run(env)

