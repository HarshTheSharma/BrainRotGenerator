import openai
import random
class ScriptGenerator:
    def __init__(self, modeSelect): # MODE 1 = FUNNY | MODE 2 = HORROR | MODE 3 = REDDIT [CURRENTLY NON-FUNCTIONAL DUE TO POORLY-WRITTEN PROMPT]
        openai.api_key = "ENTER SECRET KEY HERE"
        systemMsgArray = ['You are a writer who generates funny made up senarios for TikTok that are less than a minute long. Keep in mind that they will be read out by a single narrator.','You are a writer who writes horror senarios for TikTok that are less than a minute long. They should always end abruptly and on cliffhangers. Keep in mind that they will be read out by a single narrator as if they were in the past. Keep things scary as well.','You are a writer who generates fake reddit posts for TikTok that are less than a minute long. Keep in mind that they will be read out by a single narrator.']
        self.system_msg = systemMsgArray[modeSelect]

    def GenerateScript(self):
        messages=[{"role": "system", "content": self.system_msg}, {"role": "user", "content": 'Generate me a tiktok script to be read aloud, make sure to add a newline after every sentence. Do not use any extra formatting or appeal to the tiktok audience, this should just be directly readable word for word by a narrator. There should be no dialogue from anyone but the the person reading, it is all in the first person recalling events. Do include not "Narrator: ". Again this wil be read word for word do not include anything but the script.'}]
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = messages,
            temperature = random.uniform(0.4, 1.0),
            max_tokens = 200,
        )
        content = response.choices[0].message["content"]
        #print(content)
        return content
