import cv2
from tqdm import tqdm
from fire import Fire


def main(video_file, path_to_save):
    print(cv2.__version__)
    vidcap = cv2.VideoCapture(video_file)
    property_id = int(cv2.CAP_PROP_FRAME_COUNT)
    length = int(cv2.VideoCapture.get(vidcap, property_id))
    success, image = vidcap.read()
    count = 0
    success = True
    for i in tqdm(range(length)):
        cv2.imwrite(f"{path_to_save}/frame_{count}.jpg", image)
        success, image = vidcap.read()


if __name__ == "__main__":
    Fire(main)
