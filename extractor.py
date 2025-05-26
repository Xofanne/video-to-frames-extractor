from numpy import ndarray, uint8, stack, random
from cv2 import VideoCapture, imwrite, GaussianBlur, cvtColor, COLOR_BGR2GRAY, add
from os import path, makedirs

def add_gaussian_noise(image: ndarray, intensity=1) -> ndarray:
        '''
        Adds Gaussian noise to an image.

        Args:
                image (numpy.ndarray): The input image.
                intensity (int): Noise intensity from 1 - 3.

        Returns:
                numpy.ndarray: The noisy image.
        '''

        row, col, channels = image.shape  # shape of image is height, width, channels of colors (channels does not exists if is black and white)
        gaussian = random.normal(0, 1, (row, col, channels)).astype(uint8)  # creates random noise with image shape

        match int(intensity):  # the intensity should be consistent with any image size
                case 1:
                        intens = row//50 if row//50 % 2 != 0 else (row//50) + 1
                case 2:
                        intens = row//70 if row//70 % 2 != 0 else (row//70) + 1
                case 3:
                        intens = row//90 if row//90 % 2 != 0 else (row//90) + 1


        gaussian = GaussianBlur(gaussian, (intens, intens), 0, 0)  # aplies blur to noise to make more like film grain

        gaussian = cvtColor(gaussian, COLOR_BGR2GRAY)  # convert the noise to B&W
        gaussian = stack([gaussian]*3, axis=-1)  # if image have color, aplies the B&W to all RGB channels

        noisy_image = add(image, gaussian)  # add original frame and noise together
        return noisy_image


def extract_frames(video_path: str, frames_dir: str, add_noise: bool, grayscale: bool, overwrite: bool, intensity=1) -> int: 
        '''
        Extract frames from a video

        Args:
                video_path (str): path of the video.
                frames_dir (str): the directory to save the frames.
                add_noise (bool): if True, adds noise to extracted frames.
                grayscale (bool): if True, convert frames to grayscale.
                overwrite (bool): overwrite frames that already exist?
                step (int): extract every step frames. (Eg. extract every 2 frames.) 
                intensity (int): Noise intensity from 1 - 3.
                
        Returns: 
                int: count of images saved
        '''

        video_dir, video_filename = path.split(video_path)  # get the video path and filename from the path
        video_filename = "".join(video_filename.split(".")[0:len(video_filename.split("."))-1])
        if add_noise:
                video_filename += f"-noisy-intens-{intensity}"

        if grayscale:
                video_filename += "-B&W"


        assert path.exists(video_path), "the video file does not exist"  # assert the video file exists

        capture = VideoCapture(video_path)  # open the video file for read later
        
        if not capture.isOpened():
                print("video file could not be openned")
                exit()

        saved_count = 0  # initialize number of frames saved
        cur_frame = 0  # initialize the index of frame


        while True:
                ret, frame = capture.read()  # ret returns a bool. If True, the frame exists, False otherwise. Frame returns the actual frame data
                if not ret:
                        break
                
                if grayscale:
                        frame = cvtColor(frame, COLOR_BGR2GRAY)
                        frame = stack([frame]*3, axis=-1)

                if add_noise:
                        frame = add_gaussian_noise(frame, intensity=intensity)  # add gausian noise to frame


                save_path = path.join(frames_dir, video_filename, "{:010d}.jpg".format(cur_frame))  # creates path to save the frame

                if not path.exists(save_path) or overwrite:  # saves the frame on path.
                        imwrite(save_path, frame)
                        saved_count += 1
                
                cur_frame += 1

        print(f"terminated with -> {saved_count} frames extracted")

        return saved_count


def video_to_frame() -> str:

        video_path = input("insert the video path: ")
        video_path = path.normpath(video_path)  # make the paths OS (Windows) compatible

        frames_dir = input("insert dir name to extract the frames: ")
        frames_dir = path.normpath(frames_dir)  # make the paths OS (Windows) compatible

        video_dir, video_filename = path.split(video_path)  # get the video path and filename from the path
        video_filename = "".join(video_filename.split(".")[0:len(video_filename.split("."))-1])
        
        add_noise = input("Add noise to frames? (y/n) -> ").lower()
        assert add_noise in ["y", "n"], "please select one of two options y (yes) or n (no)"
        add_noise = True if add_noise == "y" else False

        to_grayscale = input("Convert extracted frames to grayscale? (y/n) -> ").lower()
        assert to_grayscale in ["y", "n"], "please select one of two options y (yes) or n (no)"
        to_grayscale = True if to_grayscale == "y" else False

        overwrite = input("overwrite files if already exists? (y/n) -> ").lower()
        assert overwrite in ["y", "n"], "please select one of two options y (yes) or n (no)"
        overwrite = True if overwrite == "y" else False

        intens = 0
        if add_noise:
                intens = input("Select the noise intensity from 1 to 3: ")
                assert int(intens) in [1, 2, 3], "select a number from 1 to 3"
                video_filename += f"-noisy-intens-{intens}"

        if to_grayscale:
                video_filename += "-B&W"

        makedirs(path.join(frames_dir, video_filename), exist_ok=True)  # creates the folders to extract the frames
        
        print("extracting")
        
        if extract_frames(video_path, frames_dir, add_noise, to_grayscale, overwrite, intens) == 0:
                print(f"files already exists and overwrite is set to {overwrite}")
        
        return path.join(frames_dir, video_filename)
        

def main():
        video_to_frame()


if __name__ == "__main__":
        main()