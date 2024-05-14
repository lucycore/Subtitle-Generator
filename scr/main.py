import basic_tools
from config import DockerConfig
from media import Media
from openai_api import GPTApi, WisperApi
from subtitle import SubtitleWriter, SubtitleDecoder



cfg = DockerConfig()
gpt = GPTApi(cfg("OPENAI_API_KEY_PETER"))
wis = WisperApi(cfg("OPENAI_API_KEY_PETER"))

audio_file = open(r"C:\Users\lucyc\Desktop\aaaa.mp3", "rb")
transcript = wis.transcribe_timestamp(audio_file)
print(transcript)




#----------------------------- Comst Function ---------------------------------


# def transfer_subtitle(path: str, lenth: str):
#     fvideo = FilePath(path)
#     video = Media(fvideo, SystemCmd())
#     data = []
#     wd = whisper_driver()
#     wd.model_load()
#     video.init_process()
#     while True:
#         print("[transfer_subtitle] : lenth")
#         temp_file = video.get_audio_pice(int(lenth))
#         if not temp_file:
#             break

#         wd.transcribe(temp_file)
#         wd.init_reader()
        
#         while True:
#             res = wd.get_sentence()
#             if res == (None, None, None):
#                 break

#             print("[{}:{}:{},{} ----> {}:{}:{},{}] {}".format(
#                 res[0][0], res[0][1], res[0][2], res[0][3], \
#                 res[1][0], res[1][1], res[1][2], res[1][3], res[2]))
            
#             data.append(res)
    
#     memory.write("subt_data", data)
#     subt_data_f = fvideo.nfile(full_name="subt_data.json")
#     with open(subt_data_f(), "w") as f:
#         json.dump(data, f)


# def transfer_subtitle_ch(path: str, background: str):
#     fsubt_data = FilePath(path)
#     fsubt_data_ch = fsubt_data.nfile(full_name="subt_data_ch.json")

#     subt_data_ch = []
#     subt_data = []
#     with open(fsubt_data(), "r") as f:
#         subt_data = json.load(f)

#     for i in range(len(subt_data)):
#         subtitle = subt_data[i][2]
#         prompt = "Please translate the English subtitles into Chinese. this subtitle is from "\
#             + background + ".\nSubtitle : " + subtitle + "."
        
#         for count in range(5):
#             try:
#                 subtitle_ch = gpt.query([{"role": "user", "content": prompt}], max_tokens=1000, temperature=0.0, timeout=30)
#                 break
#             except Exception as e:
#                 print(e)
#                 print("[transfer_subtitle_ch] : GPT API error, retrying...")
#                 continue
#         if count == 4:
#             input("[transfer_subtitle_ch] : GPT API error, please check your API key and network. Press any key to continue...")
#             exit(0)

#         print("[transfer_subtitle_ch] : {} ----> {}".format(subtitle, subtitle_ch))
#         subt_data_ch.append([subt_data[i][0], subt_data[i][1], subtitle_ch])
    
#     with open(fsubt_data_ch(), "w") as f:
#         json.dump(subt_data_ch, f)


# def data_to_subtitle(path: str):
#     fsubt_data_ch = FilePath(path)
#     fsub_ch_str = fsubt_data_ch.nfile(full_name="subt_ch.srt")

#     subt_data_ch = []
#     with open(fsubt_data_ch(), "r") as f:
#         subt_data_ch = json.load(f)
    
#     subt_writer = SubtitleWriter(files=fsub_ch_str)
#     subt_writer.open()
    
#     for subt in subt_data_ch:
#         # 这里我们进行了一点转换，subt[2]原本是一个字符串，但是我们需要将其转为列表
#         subt_writer.write_subtitle(subt[0], subt[1], [subt[2]])


# def get_text(file_path: str, text_lenth: int):
#     # 从文件中获取文本, 字符串长度为text_lenth
#     text = None
#     with open(file_path, "r", encoding="utf-8") as file:
#         text = file.read()
    
#     for i in range(0, len(text), text_lenth):
#         yield text[i : i + text_lenth]
#     yield text[i + text_lenth :]


# def purefy_subtitle(in_path: str, out_path: str, lenth: str):
#     text_in = FilePath(in_path)
#     text_out = text_in.nfile(full_name=out_path)
#     text_gen = get_text(text_in(), int(lenth))

#     prompt = "翻译‘<<>>’中的文本 到中文\n <<"

#     with open(text_out(), "w", encoding="utf-8") as file:
#         while True:
#             text = next(text_gen)
#             if not text:
#                 break
        
#             for count in range(5):
#                 try:
#                     summary = gpt.query([{"role": "user", "content": prompt + text + ">>"}], max_tokens=3500, temperature=0.0, timeout=30)
#                     break
#                 except Exception as e:
#                     print(e)
#                     print("[purefy_subtitle] : GPT API error, retrying...")
#                     continue
            
#             if count == 4:
#                 input("[purefy_subtitle] : GPT API error, please check your API key and network. Press any key to continue...")
#                 exit(0)
            
#             print("[purefy_subtitle] : {} ----> {}".format(text, summary))
#             file.write(summary + "\n")
#             file.flush()
    
#     print("[purefy_subtitle] : Done.")

# def purefy_all_dir(in_path: str, lenth: str):
#     for file in os.listdir(in_path):
#         if file.endswith(".txt"):
#             purefy_subtitle(in_path + "/" + file, 'purefy_'+file, lenth)


# #----------------------------- Command ---------------------------------

# def shelp():
#     print("[help] : command list:")
#     for cmd_name, func in command_list:
#         print(" --{:<10}-> {}".format(cmd_name, func.__name__))


# # ----------------------------- Command register ---------------------------------
# command_list = [
#     ("h", shelp),
#     ("mls", memory.ls_memory),
#     ("mdel", memory.del_memo),
#     ("mrename", memory.rename),
#     ("trans", transfer_subtitle),
#     ("ch", transfer_subtitle_ch),
#     ("dts", data_to_subtitle),
#     ("p", purefy_subtitle),
#     ("pall", purefy_all_dir),
#     ("q", exit)
# ] 
# # list of command and functions


# def command(cmd, *args):

#     for cmd_name, func in command_list:
#         if cmd_name == cmd:
#             func(*args)
#             return


# def main():

#     say_hello()
    
#     while True:
#         cmd = input(">>> ")
#         cmd = cmd.split("@")

#         if cmd[0] == "q":
#             break

#         command(cmd[0], *cmd[1:])
        
#         # try:
#         #     command(cmd[0], *cmd[1:])
#         # except Exception as e:
#         #     print("[main] : {}".format(e))
#         #     continue


# if "__main__" == __name__:
#     main()