from nearai.agents.environment import Environment

def run(env: Environment):
    # Your agent code here
    # agent 1
    # test 4
    prompt = {"role": "system", "content": "gh-upload-test"}
    result = env.completion([prompt] + env.list_messages())
    env.add_reply(result)
    env.request_user_input()

run(env)

