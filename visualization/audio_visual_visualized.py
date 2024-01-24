from argparse import ArgumentParser
from scipy.io import wavfile
import os,pdb,json,random

def get_random_sample():
    return random.sample('zyxwvutsrqponmlkjihgfedcba',8)

def read_rttm_duration(rttm_file_path):
    duration_dict = dict()
    duration_dict_index_to_file = dict()
    duration_dict_file_to_index = dict()

    index = 0
    for line in open(rttm_file_path).readlines():
        items = line.replace("\n","").split()
        #SPEAKER xxx 0 start duration <NA> <NA> spk_name <NA> <NA>
        filename = items[1]
        start_time = float(items[3])
        duration_time = float(items[4])
        end_time = start_time + duration_time
        speaker_name = items[7]
        if filename not in duration_dict.keys():
            duration_dict[filename] = []
            duration_dict_index_to_file[str(index)] = filename
            duration_dict_file_to_index[filename] = str(index)
            index += 1

        duration_dict[filename].append((duration_dict_file_to_index[filename],start_time, end_time,speaker_name))

    return duration_dict, duration_dict_index_to_file, duration_dict_file_to_index

def get_local_prefix(duration_dict_index_to_file):
    dict_ = dict()

    for i in duration_dict_index_to_file.keys():
        dict_[i] = ''
    return dict_


def get_file_json(duration_dict_index_to_file):
    file_json = dict()

    for index in duration_dict_index_to_file.keys():
        filename = duration_dict_index_to_file[index]
        file_json[index] = dict()
        file_json[index]["fid"] = index
        file_json[index]["fname"] = filename
        file_json[index]["type"] = 4
        file_json[index]["loc"] = 0
        file_json[index]["src"] =  "%s/mp4_files_with_faces/%s.mp4"%(os.path.abspath('.'),filename) # local file or oss file path

    return file_json


def get_duration_json(duration_dict):
    dict_ = dict()

    count = 0
    for key in duration_dict:
        for item in duration_dict[key]:
            index = item[0]
            id_ =  str(count)+ "_"+''.join(get_random_sample())
            start_time = item[1]
            end_time = item[2]
            spk_name = item[3]
            dict_[id_] = dict()
            dict_[id_]['vid'] = index
            dict_[id_]['flg'] = 0
            dict_[id_]['z'] = [start_time, end_time]
            dict_[id_]['xy'] = []
            dict_[id_]['av'] = dict()
            dict_[id_]['av']["1"] = spk_name
            dict_[id_]['av']["5"] = "0"
            count += 1
    return dict_

def get_view_dict(duration_dict_index_to_file):
    dict_ = dict()
    for index in duration_dict_index_to_file.keys():
        dict_[index] = dict()
        dict_[index]['fid_list'] = [index]
    return dict_

def generating_json(duration_dict,duration_dict_index_to_file, duration_dict_file_to_index, output_json_file):
    via_json_obj = json.load(open("via_template.json"))

    via_json_obj["config"]["ui"]["gtimeline_visible_row_count"] = 6
    via_json_obj["config"]["ui"]["file_content_align"] = "center"
    via_json_obj["config"]["ui"]["file_metadata_editor_visible"] = True
    via_json_obj["config"]["ui"]["spatial_metadata_editor_visible"] = True
    via_json_obj["config"]["ui"]["temporal_segment_metadata_editor_visible"] = True
    via_json_obj["config"]["file"] = {
                                        "loc_prefix": {
                                            "0": "",
                                        }
                                     }

    via_json_obj['project']["vid_list"] = list(duration_dict_index_to_file.keys())

    via_json_obj['config']['file']['loc_prefix'] = get_local_prefix(duration_dict_index_to_file)

    via_json_obj['file'] = get_file_json(duration_dict_index_to_file)

    via_json_obj['metadata'] = get_duration_json(duration_dict)

    via_json_obj['view'] = get_view_dict(duration_dict_index_to_file)

    open(output_json_file,"w").write(json.dumps(via_json_obj))

def main():
    parser = ArgumentParser(
        description='Speaker diarization visualization tool for audio-visual modality.', add_help=True,
        usage='%(prog)s [options]')
    parser.add_argument('-rttm', dest='rttm_fns', help='reference or system RTTM files (default: %(default)s)')
    parser.add_argument('-mp4_path', dest='video_path', help='mp4 local files (default: %(default)s)')
    parser.add_argument('-via_json_result', dest='via_json_result', help='VIA JSON output path', default='via_result.json')
    args = parser.parse_args()

    duration_dict,duration_dict_index_to_file, duration_dict_file_to_index = read_rttm_duration(args.rttm_fns)
    generating_json(duration_dict,duration_dict_index_to_file, duration_dict_file_to_index, args.via_json_result)

if __name__ == "__main__":
    main()