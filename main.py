# Unstoppable Alarm Clock
# Copyright (c) 2022 Sora Arakawa
# Licensed under the MIT License

import time
import datetime
import simpleaudio

set_hour = 8
set_minute = 0
set_time = set_hour * 60 + set_minute

while True:
	dt = datetime.datetime.now()
	get_time = dt.hour * 60 + dt.minute
	if dt.second <= 2:
		if get_time == set_time or get_time == set_time + 10 or get_time == set_time + 20 or get_time == set_time + 30 or get_time == set_time + 40 or get_time == set_time + 50 or get_time == set_time + 60:
			wav_obj = simpleaudio.WaveObject.from_wave_file("sound.wav")
			play_obj = wav_obj.play()
			play_obj.wait_done()
	time.sleep(1)
