import math
import struct
import wave
import random
import os

OUTPUT_DIR = r"c:\Users\neo31\Mailstorm\web\public\audio"
os.makedirs(OUTPUT_DIR, exist_ok=True)
FILE_PATH = os.path.join(OUTPUT_DIR, "abyssal_hum.wav")

SAMPLE_RATE = 44100
DURATION_SECONDS = 10
NUM_SAMPLES = SAMPLE_RATE * DURATION_SECONDS
MAX_AMPLITUDE = 32767

def synthesize_audio():
    print("Generating Abyssal Hum...")
    
    # Open WAV file
    wav_file = wave.open(FILE_PATH, 'w')
    wav_file.setnchannels(1)      # Mono
    wav_file.setsampwidth(2)      # 2 bytes (16-bit)
    wav_file.setframerate(SAMPLE_RATE)
    
    # We will generate a mix of frequencies to simulate a cursed fluorescent/industrial basement
    # 60 Hz - typical US mains electrical hum
    # 120 Hz - first harmonic of the electrical hum
    # 45 Hz - very low industrial sub-rumble
    
    volume_60hz = 0.4
    volume_120hz = 0.2
    volume_45hz = 0.3
    noise_vol = 0.05
    
    for i in range(NUM_SAMPLES):
        t = i / float(SAMPLE_RATE)
        
        # Sine waves
        wave_60hz = math.sin(2.0 * math.pi * 60.0 * t) * volume_60hz
        wave_120hz = math.sin(2.0 * math.pi * 120.0 * t) * volume_120hz
        wave_45hz = math.sin(2.0 * math.pi * 45.0 * t) * volume_45hz
        
        # Slight low-frequency modulation (wobble) so it isn't perfectly static
        wobble = math.sin(2.0 * math.pi * 0.5 * t) * 0.1 + 0.9 
        
        # Combine
        combined = (wave_60hz + wave_120hz + wave_45hz) * wobble
        
        # Add a tiny bit of white noise for air/ventilation sound
        noise = (random.random() * 2 - 1) * noise_vol
        combined += noise
        
        # Ensure we don't clip
        if combined > 1.0: combined = 1.0
        if combined < -1.0: combined = -1.0
        
        # Convert to 16 bit signed integer
        audio_sample = int(combined * MAX_AMPLITUDE)
        data = struct.pack('<h', audio_sample)
        wav_file.writeframesraw(data)
        
    wav_file.close()
    print(f"Abyssal Hum generated successfully at: {FILE_PATH}")

if __name__ == "__main__":
    synthesize_audio()
