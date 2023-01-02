import os
import pandas as pd
from definitions import CDLS_DIR
from modules.cdl_layout_classes import AnalogInputLayout, AnalogOutputLayout, DigitalInputLayout, DigitalOutputLayout
from modules.cdl_classes import AnalogInputChannel, AnalogOutputChannel, DigitalInputChannel, DigitalOutputChannel

def main(data):

    # print("Parsing and Loading CDL's...", end = " ")

    cdls = read_cdls()
    class_data = parse_cdls(cdls, data)
    build_layout_classes(class_data[0])
    build_channel_classes(class_data[1])

    # print("Done.")

def read_cdls():

    cdls = []

    for cdl in os.listdir(CDLS_DIR):
        if check_if_valid_cdl(cdl):
            cdl_filename = os.path.join(CDLS_DIR, cdl)
            csv = pd.read_csv(cdl_filename, header = None)
            cdls.append(csv)
        else:
            print(f"{cdl_filename} is not a valid CDL.")

    return cdls

def check_if_valid_cdl(cdl):
    if cdl.endswith('.csv'):
        valid_cdl = True
    else:
        valid_cdl = False
    return valid_cdl

def parse_cdls(cdls, data):

    section_titles = []
    section_layouts = []
    channel_data = []

    title_indices = []
    layout_indices = []

    section_layout_info = {}
    section_channel_data = {}

    for cdl in cdls:
        for index, row in cdl.iterrows():
            key = row[0]
            section_name_row = str(key).startswith('[[')

            if section_name_row:
                section_title = key[2:-2]
                title_index = index
                layout_index = title_index + 1

                section_titles.append(section_title)
                title_indices.append(title_index)
                layout_indices.append(layout_index)

            if index in layout_indices:
                cleaned_list = [x for x in row if x == x]
                section_layouts.append(cleaned_list)

            channel_types = get_channel_types(data)

            if row.isin(channel_types).any():
                cleaned_data = [x for x in row if x == x]
                channel_data.append(cleaned_data)

    for section in section_titles:
        for layout in section_layouts:
            section_layout_info[section] = layout
            section_layouts.remove(layout)
            break

    return section_layout_info, channel_data

def get_channel_types(channel_list):

    channel_types = []

    for channels in channel_list:
        data = vars(channels)
        for key in data:
            if key == 'options':
                if isinstance(data[key], list):
                    for item in data[key]:
                        channel_types.append(item)
                else:
                    channel_types.append(data[key])
    return channel_types

def build_layout_classes(class_data):

    layout_classes = []

    for key in class_data:
        if key == 'ANALOG INPUT':
            ain_layout = AnalogInputLayout(class_data[key][0],
                                            class_data[key][1],
                                            class_data[key][2],
                                            class_data[key][3],
                                            class_data[key][4],
                                            class_data[key][5],
                                            class_data[key][6],
                                            class_data[key][7],
                                            class_data[key][8])
            layout_classes.append(ain_layout)

        elif key == 'ANALOG OUTPUT':
            aout_layout = AnalogOutputLayout(class_data[key][0],
                                            class_data[key][1],
                                            class_data[key][2],
                                            class_data[key][3],
                                            class_data[key][4],
                                            class_data[key][5],
                                            class_data[key][6],
                                            class_data[key][7])
            layout_classes.append(aout_layout)

        elif key == 'DIGITAL INPUT':
            din_layout = DigitalInputLayout(class_data[key][0],
                                            class_data[key][1])
            layout_classes.append(din_layout)

        elif key == 'DIGITAL OUTPUT':
            dout_layout = DigitalOutputLayout(class_data[key][0],
                                            class_data[key][1])
            layout_classes.append(dout_layout)

        else:
            print(f'[ERROR] Invalid section.')
            continue
    return layout_classes

def build_channel_classes(channels):

    channel_list = []

    for channel in channels:
        for element in channel:
            if element == 'Current AI':
                ain_channel = AnalogInputChannel(channel[0],
                                                channel[1],
                                                channel[2],
                                                channel[3],
                                                channel[4],
                                                channel[5],
                                                channel[6],
                                                channel[7],
                                                channel[8],
                                                channel[9])
                channel_list.append(ain_channel)
            elif element == 'Current AO':
                print(channel[6])
                aout_channel = AnalogOutputChannel(channel[0],
                                                channel[1],
                                                channel[2],
                                                channel[3],
                                                channel[4],
                                                channel[5],
                                                channel[6],
                                                channel[7],
                                                channel[8])
                channel_list.append(aout_channel)
            elif element == 'Digital DI':
                din_channel = DigitalInputChannel(channel[0],
                                                channel[1],
                                                channel[2])
                channel_list.append(din_channel)
            elif element == 'Digital DO':
                dout_channel = DigitalOutputChannel(channel[0],
                                                channel[1],
                                                channel[2])
                channel_list.append(dout_channel)

    for item in channel_list:
        print(vars(item))