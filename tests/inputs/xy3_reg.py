import numpy as np

xy3_reg = np.array(
[[0.0000,0.0000],
[0.0100,0.0050],
[0.0200,0.0100],
[0.0300,0.0150],
[0.0400,0.0200],
[0.0500,0.0250],
[0.0600,0.0300],
[0.0700,0.0350],
[0.0800,0.0400],
[0.0900,0.0450],
[0.1000,0.0500],
[0.1100,0.0550],
[0.1200,0.0600],
[0.1300,0.0650],
[0.1400,0.0700],
[0.1500,0.0750],
[0.1600,0.0800],
[0.1700,0.0850],
[0.1800,0.0900],
[0.1900,0.0950],
[0.2000,0.1000],
[0.2100,0.1050],
[0.2200,0.1100],
[0.2300,0.1150],
[0.2400,0.1200],
[0.2500,0.1250],
[0.2600,0.1300],
[0.2700,0.1350],
[0.2800,0.1400],
[0.2900,0.1450],
[0.3000,0.1500],
[0.3100,0.1550],
[0.3200,0.1600],
[0.3300,0.1650],
[0.3400,0.1700],
[0.3500,0.1750],
[0.3600,0.1800],
[0.3700,0.1850],
[0.3800,0.1900],
[0.3900,0.1950],
[0.4000,0.2000],
[0.4100,0.2050],
[0.4200,0.2100],
[0.4300,0.2150],
[0.4400,0.2200],
[0.4500,0.2250],
[0.4600,0.2300],
[0.4700,0.2350],
[0.4800,0.2400],
[0.4900,0.2450],
[0.5000,0.2500],
[0.5100,0.2550],
[0.5200,0.2600],
[0.5300,0.2650],
[0.5400,0.2700],
[0.5500,0.2750],
[0.5600,0.2800],
[0.5700,0.2850],
[0.5800,0.2900],
[0.5900,0.2950],
[0.6000,0.3000],
[0.6100,0.3050],
[0.6200,0.3100],
[0.6300,0.3150],
[0.6400,0.3200],
[0.6500,0.3250],
[0.6600,0.3300],
[0.6700,0.3350],
[0.6800,0.3400],
[0.6900,0.3450],
[0.7000,0.3500],
[0.7100,0.3550],
[0.7200,0.3600],
[0.7300,0.3650],
[0.7400,0.3700],
[0.7500,0.3750],
[0.7600,0.3800],
[0.7700,0.3850],
[0.7800,0.3900],
[0.7900,0.3950],
[0.8000,0.4000],
[0.8100,0.4050],
[0.8200,0.4100],
[0.8300,0.4150],
[0.8400,0.4200],
[0.8500,0.4250],
[0.8600,0.4300],
[0.8700,0.4350],
[0.8800,0.4400],
[0.8900,0.4450],
[0.9000,0.4500],
[0.9100,0.4550],
[0.9200,0.4600],
[0.9300,0.4650],
[0.9400,0.4700],
[0.9500,0.4750],
[0.9600,0.4800],
[0.9700,0.4850],
[0.9800,0.4900],
[0.9900,0.4950],
[1.0000,0.5000],
[1.0100,0.5050],
[1.0200,0.5100],
[1.0300,0.5150],
[1.0400,0.5200],
[1.0500,0.5250],
[1.0600,0.5300],
[1.0700,0.5350],
[1.0800,0.5400],
[1.0900,0.5450],
[1.1000,0.5500],
[1.1100,0.5550],
[1.1200,0.5600],
[1.1300,0.5650],
[1.1400,0.5700],
[1.1500,0.5750],
[1.1600,0.5800],
[1.1700,0.5850],
[1.1800,0.5900],
[1.1900,0.5950],
[1.2000,0.6000],
[1.2100,0.6050],
[1.2200,0.6100],
[1.2300,0.6150],
[1.2400,0.6200],
[1.2500,0.6250],
[1.2600,0.6300],
[1.2700,0.6350],
[1.2800,0.6400],
[1.2900,0.6450],
[1.3000,0.6500],
[1.3100,0.6550],
[1.3200,0.6600],
[1.3300,0.6650],
[1.3400,0.6700],
[1.3500,0.6750],
[1.3600,0.6800],
[1.3700,0.6850],
[1.3800,0.6900],
[1.3900,0.6950],
[1.4000,0.7000],
[1.4100,0.7050],
[1.4200,0.7100],
[1.4300,0.7150],
[1.4400,0.7200],
[1.4500,0.7250],
[1.4600,0.7300],
[1.4700,0.7350],
[1.4800,0.7400],
[1.4900,0.7450],
[1.5000,0.7500],
[1.5100,0.7550],
[1.5200,0.7600],
[1.5300,0.7650],
[1.5400,0.7700],
[1.5500,0.7750],
[1.5600,0.7800],
[1.5700,0.7850],
[1.5800,0.7900],
[1.5900,0.7950],
[1.6000,0.8000],
[1.6100,0.8050],
[1.6200,0.8100],
[1.6300,0.8150],
[1.6400,0.8200],
[1.6500,0.8250],
[1.6600,0.8300],
[1.6700,0.8350],
[1.6800,0.8400],
[1.6900,0.8450],
[1.7000,0.8500],
[1.7100,0.8550],
[1.7200,0.8600],
[1.7300,0.8650],
[1.7400,0.8700],
[1.7500,0.8750],
[1.7600,0.8800],
[1.7700,0.8850],
[1.7800,0.8900],
[1.7900,0.8950],
[1.8000,0.9000],
[1.8100,0.9050],
[1.8200,0.9100],
[1.8300,0.9150],
[1.8400,0.9200],
[1.8500,0.9250],
[1.8600,0.9300],
[1.8700,0.9350],
[1.8800,0.9400],
[1.8900,0.9450],
[1.9000,0.9500],
[1.9100,0.9550],
[1.9200,0.9600],
[1.9300,0.9650],
[1.9400,0.9700],
[1.9500,0.9750],
[1.9600,0.9800],
[1.9700,0.9850],
[1.9800,0.9900],
[1.9900,0.9950],
[2.0000,1.0000],
[2.0100,1.0050],
[2.0200,1.0100],
[2.0300,1.0150],
[2.0400,1.0200],
[2.0500,1.0250],
[2.0600,1.0300],
[2.0700,1.0350],
[2.0800,1.0400],
[2.0900,1.0450],
[2.1000,1.0500],
[2.1100,1.0550],
[2.1200,1.0600],
[2.1300,1.0650],
[2.1400,1.0700],
[2.1500,1.0750],
[2.1600,1.0800],
[2.1700,1.0850],
[2.1800,1.0900],
[2.1900,1.0950],
[2.2000,1.1000],
[2.2100,1.1050],
[2.2200,1.1100],
[2.2300,1.1150],
[2.2400,1.1200],
[2.2500,1.1250],
[2.2600,1.1300],
[2.2700,1.1350],
[2.2800,1.1400],
[2.2900,1.1450],
[2.3000,1.1500],
[2.3100,1.1550],
[2.3200,1.1600],
[2.3300,1.1650],
[2.3400,1.1700],
[2.3500,1.1750],
[2.3600,1.1800],
[2.3700,1.1850],
[2.3800,1.1900],
[2.3900,1.1950],
[2.4000,1.2000],
[2.4100,1.2050],
[2.4200,1.2100],
[2.4300,1.2150],
[2.4400,1.2200],
[2.4500,1.2250],
[2.4600,1.2300],
[2.4700,1.2350],
[2.4800,1.2400],
[2.4900,1.2450],
[2.5000,1.2500],
[2.5100,1.2550],
[2.5200,1.2600],
[2.5300,1.2650],
[2.5400,1.2700],
[2.5500,1.2750],
[2.5600,1.2800],
[2.5700,1.2850],
[2.5800,1.2900],
[2.5900,1.2950],
[2.6000,1.3000],
[2.6100,1.3050],
[2.6200,1.3100],
[2.6300,1.3150],
[2.6400,1.3200],
[2.6500,1.3250],
[2.6600,1.3300],
[2.6700,1.3350],
[2.6800,1.3400],
[2.6900,1.3450],
[2.7000,1.3500],
[2.7100,1.3550],
[2.7200,1.3600],
[2.7300,1.3650],
[2.7400,1.3700],
[2.7500,1.3750],
[2.7600,1.3800],
[2.7700,1.3850],
[2.7800,1.3900],
[2.7900,1.3950],
[2.8000,1.4000],
[2.8100,1.4050],
[2.8200,1.4100],
[2.8300,1.4150],
[2.8400,1.4200],
[2.8500,1.4250],
[2.8600,1.4300],
[2.8700,1.4350],
[2.8800,1.4400],
[2.8900,1.4450],
[2.9000,1.4500],
[2.9100,1.4550],
[2.9200,1.4600],
[2.9300,1.4650],
[2.9400,1.4700],
[2.9500,1.4750],
[2.9600,1.4800],
[2.9700,1.4850],
[2.9800,1.4900],
[2.9900,1.4950],
[3.0000,1.5000],
[3.0100,1.5050],
[3.0200,1.5100],
[3.0300,1.5150],
[3.0400,1.5200],
[3.0500,1.5250],
[3.0600,1.5300],
[3.0700,1.5350],
[3.0800,1.5400],
[3.0900,1.5450],
[3.1000,1.5500],
[3.1100,1.5550],
[3.1200,1.5600],
[3.1300,1.5650],
[3.1400,1.5700],
[3.1500,1.5750],
[3.1600,1.5800],
[3.1700,1.5850],
[3.1800,1.5900],
[3.1900,1.5950],
[3.2000,1.6000],
[3.2100,1.6050],
[3.2200,1.6100],
[3.2300,1.6150],
[3.2400,1.6200],
[3.2500,1.6250],
[3.2600,1.6300],
[3.2700,1.6350],
[3.2800,1.6400],
[3.2900,1.6450],
[3.3000,1.6500],
[3.3100,1.6550],
[3.3200,1.6600],
[3.3300,1.6650],
[3.3400,1.6700],
[3.3500,1.6750],
[3.3600,1.6800],
[3.3700,1.6850],
[3.3800,1.6900],
[3.3900,1.6950],
[3.4000,1.7000],
[3.4100,1.7050],
[3.4200,1.7100],
[3.4300,1.7150],
[3.4400,1.7200],
[3.4500,1.7250],
[3.4600,1.7300],
[3.4700,1.7350],
[3.4800,1.7400],
[3.4900,1.7450],
[3.5000,1.7500],
[3.5100,1.7550],
[3.5200,1.7600],
[3.5300,1.7650],
[3.5400,1.7700],
[3.5500,1.7750],
[3.5600,1.7800],
[3.5700,1.7850],
[3.5800,1.7900],
[3.5900,1.7950],
[3.6000,1.8000],
[3.6100,1.8050],
[3.6200,1.8100],
[3.6300,1.8150],
[3.6400,1.8200],
[3.6500,1.8250],
[3.6600,1.8300],
[3.6700,1.8350],
[3.6800,1.8400],
[3.6900,1.8450],
[3.7000,1.8500],
[3.7100,1.8550],
[3.7200,1.8600],
[3.7300,1.8650],
[3.7400,1.8700],
[3.7500,1.8750],
[3.7600,1.8800],
[3.7700,1.8850],
[3.7800,1.8900],
[3.7900,1.8950],
[3.8000,1.9000],
[3.8100,1.9050],
[3.8200,1.9100],
[3.8300,1.9150],
[3.8400,1.9200],
[3.8500,1.9250],
[3.8600,1.9300],
[3.8700,1.9350],
[3.8800,1.9400],
[3.8900,1.9450],
[3.9000,1.9500],
[3.9100,1.9550],
[3.9200,1.9600],
[3.9300,1.9650],
[3.9400,1.9700],
[3.9500,1.9750],
[3.9600,1.9800],
[3.9700,1.9850],
[3.9800,1.9900],
[3.9900,1.9950],
[4.0000,2.0000],
[4.0100,2.0050],
[4.0200,2.0100],
[4.0300,2.0150],
[4.0400,2.0200],
[4.0500,2.0250],
[4.0600,2.0300],
[4.0700,2.0350],
[4.0800,2.0400],
[4.0900,2.0450],
[4.1000,2.0500],
[4.1100,2.0550],
[4.1200,2.0600],
[4.1300,2.0650],
[4.1400,2.0700],
[4.1500,2.0750],
[4.1600,2.0800],
[4.1700,2.0850],
[4.1800,2.0900],
[4.1900,2.0950],
[4.2000,2.1000],
[4.2100,2.1050],
[4.2200,2.1100],
[4.2300,2.1150],
[4.2400,2.1200],
[4.2500,2.1250],
[4.2600,2.1300],
[4.2700,2.1350],
[4.2800,2.1400],
[4.2900,2.1450],
[4.3000,2.1500],
[4.3100,2.1550],
[4.3200,2.1600],
[4.3300,2.1650],
[4.3400,2.1700],
[4.3500,2.1750],
[4.3600,2.1800],
[4.3700,2.1850],
[4.3800,2.1900],
[4.3900,2.1950],
[4.4000,2.2000],
[4.4100,2.2050],
[4.4200,2.2100],
[4.4300,2.2150],
[4.4400,2.2200],
[4.4500,2.2250],
[4.4600,2.2300],
[4.4700,2.2350],
[4.4800,2.2400],
[4.4900,2.2450],
[4.5000,2.2500],
[4.5100,2.2550],
[4.5200,2.2600],
[4.5300,2.2650],
[4.5400,2.2700],
[4.5500,2.2750],
[4.5600,2.2800],
[4.5700,2.2850],
[4.5800,2.2900],
[4.5900,2.2950],
[4.6000,2.3000],
[4.6100,2.3050],
[4.6200,2.3100],
[4.6300,2.3150],
[4.6400,2.3200],
[4.6500,2.3250],
[4.6600,2.3300],
[4.6700,2.3350],
[4.6800,2.3400],
[4.6900,2.3450],
[4.7000,2.3500],
[4.7100,2.3550],
[4.7200,2.3600],
[4.7300,2.3650],
[4.7400,2.3700],
[4.7500,2.3750],
[4.7600,2.3800],
[4.7700,2.3850],
[4.7800,2.3900],
[4.7900,2.3950],
[4.8000,2.4000],
[4.8100,2.4050],
[4.8200,2.4100],
[4.8300,2.4150],
[4.8400,2.4200],
[4.8500,2.4250],
[4.8600,2.4300],
[4.8700,2.4350],
[4.8800,2.4400],
[4.8900,2.4450],
[4.9000,2.4500],
[4.9100,2.4550],
[4.9200,2.4600],
[4.9300,2.4650],
[4.9400,2.4700],
[4.9500,2.4750],
[4.9600,2.4800],
[4.9700,2.4850],
[4.9800,2.4900],
[4.9900,2.4950],
[5.0000,2.5000],
[5.0100,2.5050],
[5.0200,2.5100],
[5.0300,2.5150],
[5.0400,2.5200],
[5.0500,2.5250],
[5.0600,2.5300],
[5.0700,2.5350],
[5.0800,2.5400],
[5.0900,2.5450],
[5.1000,2.5500],
[5.1100,2.5550],
[5.1200,2.5600],
[5.1300,2.5650],
[5.1400,2.5700],
[5.1500,2.5750],
[5.1600,2.5800],
[5.1700,2.5850],
[5.1800,2.5900],
[5.1900,2.5950],
[5.2000,2.6000],
[5.2100,2.6050],
[5.2200,2.6100],
[5.2300,2.6150],
[5.2400,2.6200],
[5.2500,2.6250],
[5.2600,2.6300],
[5.2700,2.6350],
[5.2800,2.6400],
[5.2900,2.6450],
[5.3000,2.6500],
[5.3100,2.6550],
[5.3200,2.6600],
[5.3300,2.6650],
[5.3400,2.6700],
[5.3500,2.6750],
[5.3600,2.6800],
[5.3700,2.6850],
[5.3800,2.6900],
[5.3900,2.6950],
[5.4000,2.7000],
[5.4100,2.7050],
[5.4200,2.7100],
[5.4300,2.7150],
[5.4400,2.7200],
[5.4500,2.7250],
[5.4600,2.7300],
[5.4700,2.7350],
[5.4800,2.7400],
[5.4900,2.7450],
[5.5000,2.7500],
[5.5100,2.7550],
[5.5200,2.7600],
[5.5300,2.7650],
[5.5400,2.7700],
[5.5500,2.7750],
[5.5600,2.7800],
[5.5700,2.7850],
[5.5800,2.7900],
[5.5900,2.7950],
[5.6000,2.8000],
[5.6100,2.8050],
[5.6200,2.8100],
[5.6300,2.8150],
[5.6400,2.8200],
[5.6500,2.8250],
[5.6600,2.8300],
[5.6700,2.8350],
[5.6800,2.8400],
[5.6900,2.8450],
[5.7000,2.8500],
[5.7100,2.8550],
[5.7200,2.8600],
[5.7300,2.8650],
[5.7400,2.8700],
[5.7500,2.8750],
[5.7600,2.8800],
[5.7700,2.8850],
[5.7800,2.8900],
[5.7900,2.8950],
[5.8000,2.9000],
[5.8100,2.9050],
[5.8200,2.9100],
[5.8300,2.9150],
[5.8400,2.9200],
[5.8500,2.9250],
[5.8600,2.9300],
[5.8700,2.9350],
[5.8800,2.9400],
[5.8900,2.9450],
[5.9000,2.9500],
[5.9100,2.9550],
[5.9200,2.9600],
[5.9300,2.9650],
[5.9400,2.9700],
[5.9500,2.9750],
[5.9600,2.9800],
[5.9700,2.9850],
[5.9800,2.9900],
[5.9900,2.9950],
[6.0000,3.0000],
[6.0100,3.0050],
[6.0200,3.0100],
[6.0300,3.0150],
[6.0400,3.0200],
[6.0500,3.0250],
[6.0600,3.0300],
[6.0700,3.0350],
[6.0800,3.0400],
[6.0900,3.0450],
[6.1000,3.0500],
[6.1100,3.0550],
[6.1200,3.0600],
[6.1300,3.0650],
[6.1400,3.0700],
[6.1500,3.0750],
[6.1600,3.0800],
[6.1700,3.0850],
[6.1800,3.0900],
[6.1900,3.0950],
[6.2000,3.1000],
[6.2100,3.1050],
[6.2200,3.1100],
[6.2300,3.1150],
[6.2400,3.1200],
[6.2500,3.1250],
[6.2600,3.1300],
[6.2700,3.1350],
[6.2800,3.1400],
[6.2900,3.1450],
[6.3000,3.1500],
[6.3100,3.1550],
[6.3200,3.1600],
[6.3300,3.1650],
[6.3400,3.1700],
[6.3500,3.1750],
[6.3600,3.1800],
[6.3700,3.1850],
[6.3800,3.1900],
[6.3900,3.1950],
[6.4000,3.2000],
[6.4100,3.2050],
[6.4200,3.2100],
[6.4300,3.2150],
[6.4400,3.2200],
[6.4500,3.2250],
[6.4600,3.2300],
[6.4700,3.2350],
[6.4800,3.2400],
[6.4900,3.2450],
[6.5000,3.2500],
[6.5100,3.2550],
[6.5200,3.2600],
[6.5300,3.2650],
[6.5400,3.2700],
[6.5500,3.2750],
[6.5600,3.2800],
[6.5700,3.2850],
[6.5800,3.2900],
[6.5900,3.2950],
[6.6000,3.3000],
[6.6100,3.3050],
[6.6200,3.3100],
[6.6300,3.3150],
[6.6400,3.3200],
[6.6500,3.3250],
[6.6600,3.3300],
[6.6700,3.3350],
[6.6800,3.3400],
[6.6900,3.3450],
[6.7000,3.3500],
[6.7100,3.3550],
[6.7200,3.3600],
[6.7300,3.3650],
[6.7400,3.3700],
[6.7500,3.3750],
[6.7600,3.3800],
[6.7700,3.3850],
[6.7800,3.3900],
[6.7900,3.3950],
[6.8000,3.4000],
[6.8100,3.4050],
[6.8200,3.4100],
[6.8300,3.4150],
[6.8400,3.4200],
[6.8500,3.4250],
[6.8600,3.4300],
[6.8700,3.4350],
[6.8800,3.4400],
[6.8900,3.4450],
[6.9000,3.4500],
[6.9100,3.4550],
[6.9200,3.4600],
[6.9300,3.4650],
[6.9400,3.4700],
[6.9500,3.4750],
[6.9600,3.4800],
[6.9700,3.4850],
[6.9800,3.4900],
[6.9900,3.4950],
[7.0000,3.5000],
[7.0100,3.5050],
[7.0200,3.5100],
[7.0300,3.5150],
[7.0400,3.5200],
[7.0500,3.5250],
[7.0600,3.5300],
[7.0700,3.5350],
[7.0800,3.5400],
[7.0900,3.5450],
[7.1000,3.5500],
[7.1100,3.5550],
[7.1200,3.5600],
[7.1300,3.5650],
[7.1400,3.5700],
[7.1500,3.5750],
[7.1600,3.5800],
[7.1700,3.5850],
[7.1800,3.5900],
[7.1900,3.5950],
[7.2000,3.6000],
[7.2100,3.6050],
[7.2200,3.6100],
[7.2300,3.6150],
[7.2400,3.6200],
[7.2500,3.6250],
[7.2600,3.6300],
[7.2700,3.6350],
[7.2800,3.6400],
[7.2900,3.6450],
[7.3000,3.6500],
[7.3100,3.6550],
[7.3200,3.6600],
[7.3300,3.6650],
[7.3400,3.6700],
[7.3500,3.6750],
[7.3600,3.6800],
[7.3700,3.6850],
[7.3800,3.6900],
[7.3900,3.6950],
[7.4000,3.7000],
[7.4100,3.7050],
[7.4200,3.7100],
[7.4300,3.7150],
[7.4400,3.7200],
[7.4500,3.7250],
[7.4600,3.7300],
[7.4700,3.7350],
[7.4800,3.7400],
[7.4900,3.7450],
[7.5000,3.7500],
[7.5100,3.7550],
[7.5200,3.7600],
[7.5300,3.7650],
[7.5400,3.7700],
[7.5500,3.7750],
[7.5600,3.7800],
[7.5700,3.7850],
[7.5800,3.7900],
[7.5900,3.7950],
[7.6000,3.8000],
[7.6100,3.8050],
[7.6200,3.8100],
[7.6300,3.8150],
[7.6400,3.8200],
[7.6500,3.8250],
[7.6600,3.8300],
[7.6700,3.8350],
[7.6800,3.8400],
[7.6900,3.8450],
[7.7000,3.8500],
[7.7100,3.8550],
[7.7200,3.8600],
[7.7300,3.8650],
[7.7400,3.8700],
[7.7500,3.8750],
[7.7600,3.8800],
[7.7700,3.8850],
[7.7800,3.8900],
[7.7900,3.8950],
[7.8000,3.9000],
[7.8100,3.9050],
[7.8200,3.9100],
[7.8300,3.9150],
[7.8400,3.9200],
[7.8500,3.9250],
[7.8600,3.9300],
[7.8700,3.9350],
[7.8800,3.9400],
[7.8900,3.9450],
[7.9000,3.9500],
[7.9100,3.9550],
[7.9200,3.9600],
[7.9300,3.9650],
[7.9400,3.9700],
[7.9500,3.9750],
[7.9600,3.9800],
[7.9700,3.9850],
[7.9800,3.9900],
[7.9900,3.9950],
[8.0000,4.0000],
[8.0100,4.0050],
[8.0200,4.0100],
[8.0300,4.0150],
[8.0400,4.0200],
[8.0500,4.0250],
[8.0600,4.0300],
[8.0700,4.0350],
[8.0800,4.0400],
[8.0900,4.0450],
[8.1000,4.0500],
[8.1100,4.0550],
[8.1200,4.0600],
[8.1300,4.0650],
[8.1400,4.0700],
[8.1500,4.0750],
[8.1600,4.0800],
[8.1700,4.0850],
[8.1800,4.0900],
[8.1900,4.0950],
[8.2000,4.1000],
[8.2100,4.1050],
[8.2200,4.1100],
[8.2300,4.1150],
[8.2400,4.1200],
[8.2500,4.1250],
[8.2600,4.1300],
[8.2700,4.1350],
[8.2800,4.1400],
[8.2900,4.1450],
[8.3000,4.1500],
[8.3100,4.1550],
[8.3200,4.1600],
[8.3300,4.1650],
[8.3400,4.1700],
[8.3500,4.1750],
[8.3600,4.1800],
[8.3700,4.1850],
[8.3800,4.1900],
[8.3900,4.1950],
[8.4000,4.2000],
[8.4100,4.2050],
[8.4200,4.2100],
[8.4300,4.2150],
[8.4400,4.2200],
[8.4500,4.2250],
[8.4600,4.2300],
[8.4700,4.2350],
[8.4800,4.2400],
[8.4900,4.2450],
[8.5000,4.2500],
[8.5100,4.2550],
[8.5200,4.2600],
[8.5300,4.2650],
[8.5400,4.2700],
[8.5500,4.2750],
[8.5600,4.2800],
[8.5700,4.2850],
[8.5800,4.2900],
[8.5900,4.2950],
[8.6000,4.3000],
[8.6100,4.3050],
[8.6200,4.3100],
[8.6300,4.3150],
[8.6400,4.3200],
[8.6500,4.3250],
[8.6600,4.3300],
[8.6700,4.3350],
[8.6800,4.3400],
[8.6900,4.3450],
[8.7000,4.3500],
[8.7100,4.3550],
[8.7200,4.3600],
[8.7300,4.3650],
[8.7400,4.3700],
[8.7500,4.3750],
[8.7600,4.3800],
[8.7700,4.3850],
[8.7800,4.3900],
[8.7900,4.3950],
[8.8000,4.4000],
[8.8100,4.4050],
[8.8200,4.4100],
[8.8300,4.4150],
[8.8400,4.4200],
[8.8500,4.4250],
[8.8600,4.4300],
[8.8700,4.4350],
[8.8800,4.4400],
[8.8900,4.4450],
[8.9000,4.4500],
[8.9100,4.4550],
[8.9200,4.4600],
[8.9300,4.4650],
[8.9400,4.4700],
[8.9500,4.4750],
[8.9600,4.4800],
[8.9700,4.4850],
[8.9800,4.4900],
[8.9900,4.4950],
[9.0000,4.5000],
[9.0100,4.5050],
[9.0200,4.5100],
[9.0300,4.5150],
[9.0400,4.5200],
[9.0500,4.5250],
[9.0600,4.5300],
[9.0700,4.5350],
[9.0800,4.5400],
[9.0900,4.5450],
[9.1000,4.5500],
[9.1100,4.5550],
[9.1200,4.5600],
[9.1300,4.5650],
[9.1400,4.5700],
[9.1500,4.5750],
[9.1600,4.5800],
[9.1700,4.5850],
[9.1800,4.5900],
[9.1900,4.5950],
[9.2000,4.6000],
[9.2100,4.6050],
[9.2200,4.6100],
[9.2300,4.6150],
[9.2400,4.6200],
[9.2500,4.6250],
[9.2600,4.6300],
[9.2700,4.6350],
[9.2800,4.6400],
[9.2900,4.6450],
[9.3000,4.6500],
[9.3100,4.6550],
[9.3200,4.6600],
[9.3300,4.6650],
[9.3400,4.6700],
[9.3500,4.6750],
[9.3600,4.6800],
[9.3700,4.6850],
[9.3800,4.6900],
[9.3900,4.6950],
[9.4000,4.7000],
[9.4100,4.7050],
[9.4200,4.7100],
[9.4300,4.7150],
[9.4400,4.7200],
[9.4500,4.7250],
[9.4600,4.7300],
[9.4700,4.7350],
[9.4800,4.7400],
[9.4900,4.7450],
[9.5000,4.7500],
[9.5100,4.7550],
[9.5200,4.7600],
[9.5300,4.7650],
[9.5400,4.7700],
[9.5500,4.7750],
[9.5600,4.7800],
[9.5700,4.7850],
[9.5800,4.7900],
[9.5900,4.7950],
[9.6000,4.8000],
[9.6100,4.8050],
[9.6200,4.8100],
[9.6300,4.8150],
[9.6400,4.8200],
[9.6500,4.8250],
[9.6600,4.8300],
[9.6700,4.8350],
[9.6800,4.8400],
[9.6900,4.8450],
[9.7000,4.8500],
[9.7100,4.8550],
[9.7200,4.8600],
[9.7300,4.8650],
[9.7400,4.8700],
[9.7500,4.8750],
[9.7600,4.8800],
[9.7700,4.8850],
[9.7800,4.8900],
[9.7900,4.8950],
[9.8000,4.9000],
[9.8100,4.9050],
[9.8200,4.9100],
[9.8300,4.9150],
[9.8400,4.9200],
[9.8500,4.9250],
[9.8600,4.9300],
[9.8700,4.9350],
[9.8800,4.9400],
[9.8900,4.9450],
[9.9000,4.9500],
[9.9100,4.9550],
[9.9200,4.9600],
[9.9300,4.9650],
[9.9400,4.9700],
[9.9500,4.9750],
[9.9600,4.9800],
[9.9700,4.9850],
[9.9800,4.9900],
[9.9900,4.9950],
[10.0000,5.0000],
[10.0100,5.0050],
[10.0200,5.0100],
[10.0300,5.0150],
[10.0400,5.0200],
[10.0500,5.0250],
[10.0600,5.0300],
[10.0700,5.0350],
[10.0800,5.0400],
[10.0900,5.0450],
[10.1000,5.0500],
[10.1100,5.0550],
[10.1200,5.0600],
[10.1300,5.0650],
[10.1400,5.0700],
[10.1500,5.0750],
[10.1600,5.0800],
[10.1700,5.0850],
[10.1800,5.0900],
[10.1900,5.0950],
[10.2000,5.1000],
[10.2100,5.1050],
[10.2200,5.1100],
[10.2300,5.1150],
[10.2400,5.1200],
[10.2500,5.1250],
[10.2600,5.1300],
[10.2700,5.1350],
[10.2800,5.1400],
[10.2900,5.1450],
[10.3000,5.1500],
[10.3100,5.1550],
[10.3200,5.1600],
[10.3300,5.1650],
[10.3400,5.1700],
[10.3500,5.1750],
[10.3600,5.1800],
[10.3700,5.1850],
[10.3800,5.1900],
[10.3900,5.1950],
[10.4000,5.2000],
[10.4100,5.2050],
[10.4200,5.2100],
[10.4300,5.2150],
[10.4400,5.2200],
[10.4500,5.2250],
[10.4600,5.2300],
[10.4700,5.2350],
[10.4800,5.2400],
[10.4900,5.2450],
[10.5000,5.2500],
[10.5100,5.2550],
[10.5200,5.2600],
[10.5300,5.2650],
[10.5400,5.2700],
[10.5500,5.2750],
[10.5600,5.2800],
[10.5700,5.2850],
[10.5800,5.2900],
[10.5900,5.2950],
[10.6000,5.3000],
[10.6100,5.3050],
[10.6200,5.3100],
[10.6300,5.3150],
[10.6400,5.3200],
[10.6500,5.3250],
[10.6600,5.3300],
[10.6700,5.3350],
[10.6800,5.3400],
[10.6900,5.3450],
[10.7000,5.3500],
[10.7100,5.3550],
[10.7200,5.3600],
[10.7300,5.3650],
[10.7400,5.3700],
[10.7500,5.3750],
[10.7600,5.3800],
[10.7700,5.3850],
[10.7800,5.3900],
[10.7900,5.3950],
[10.8000,5.4000],
[10.8100,5.4050],
[10.8200,5.4100],
[10.8300,5.4150],
[10.8400,5.4200],
[10.8500,5.4250],
[10.8600,5.4300],
[10.8700,5.4350],
[10.8800,5.4400],
[10.8900,5.4450],
[10.9000,5.4500],
[10.9100,5.4550],
[10.9200,5.4600],
[10.9300,5.4650],
[10.9400,5.4700],
[10.9500,5.4750],
[10.9600,5.4800],
[10.9700,5.4850],
[10.9800,5.4900],
[10.9900,5.4950],
[11.0000,5.5000],
[11.0100,5.5050],
[11.0200,5.5100],
[11.0300,5.5150],
[11.0400,5.5200],
[11.0500,5.5250],
[11.0600,5.5300],
[11.0700,5.5350],
[11.0800,5.5400],
[11.0900,5.5450],
[11.1000,5.5500],
[11.1100,5.5550],
[11.1200,5.5600],
[11.1300,5.5650],
[11.1400,5.5700],
[11.1500,5.5750],
[11.1600,5.5800],
[11.1700,5.5850],
[11.1800,5.5900],
[11.1900,5.5950],
[11.2000,5.6000],
[11.2100,5.6050],
[11.2200,5.6100],
[11.2300,5.6150],
[11.2400,5.6200],
[11.2500,5.6250],
[11.2600,5.6300],
[11.2700,5.6350],
[11.2800,5.6400],
[11.2900,5.6450],
[11.3000,5.6500],
[11.3100,5.6550],
[11.3200,5.6600],
[11.3300,5.6650],
[11.3400,5.6700],
[11.3500,5.6750],
[11.3600,5.6800],
[11.3700,5.6850],
[11.3800,5.6900],
[11.3900,5.6950],
[11.4000,5.7000],
[11.4100,5.7050],
[11.4200,5.7100],
[11.4300,5.7150],
[11.4400,5.7200],
[11.4500,5.7250],
[11.4600,5.7300],
[11.4700,5.7350],
[11.4800,5.7400],
[11.4900,5.7450],
[11.5000,5.7500],
[11.5100,5.7550],
[11.5200,5.7600],
[11.5300,5.7650],
[11.5400,5.7700],
[11.5500,5.7750],
[11.5600,5.7800],
[11.5700,5.7850],
[11.5800,5.7900],
[11.5900,5.7950],
[11.6000,5.8000],
[11.6100,5.8050],
[11.6200,5.8100],
[11.6300,5.8150],
[11.6400,5.8200],
[11.6500,5.8250],
[11.6600,5.8300],
[11.6700,5.8350],
[11.6800,5.8400],
[11.6900,5.8450],
[11.7000,5.8500],
[11.7100,5.8550],
[11.7200,5.8600],
[11.7300,5.8650],
[11.7400,5.8700],
[11.7500,5.8750],
[11.7600,5.8800],
[11.7700,5.8850],
[11.7800,5.8900],
[11.7900,5.8950],
[11.8000,5.9000],
[11.8100,5.9050],
[11.8200,5.9100],
[11.8300,5.9150],
[11.8400,5.9200],
[11.8500,5.9250],
[11.8600,5.9300],
[11.8700,5.9350],
[11.8800,5.9400],
[11.8900,5.9450],
[11.9000,5.9500],
[11.9100,5.9550],
[11.9200,5.9600],
[11.9300,5.9650],
[11.9400,5.9700],
[11.9500,5.9750],
[11.9600,5.9800],
[11.9700,5.9850],
[11.9800,5.9900],
[11.9900,5.9950],
[12.0000,6.0000],
[12.0100,6.0050],
[12.0200,6.0100],
[12.0300,6.0150],
[12.0400,6.0200],
[12.0500,6.0250],
[12.0600,6.0300],
[12.0700,6.0350],
[12.0800,6.0400],
[12.0900,6.0450],
[12.1000,6.0500],
[12.1100,6.0550],
[12.1200,6.0600],
[12.1300,6.0650],
[12.1400,6.0700],
[12.1500,6.0750],
[12.1600,6.0800],
[12.1700,6.0850],
[12.1800,6.0900],
[12.1900,6.0950],
[12.2000,6.1000],
[12.2100,6.1050],
[12.2200,6.1100],
[12.2300,6.1150],
[12.2400,6.1200],
[12.2500,6.1250],
[12.2600,6.1300],
[12.2700,6.1350],
[12.2800,6.1400],
[12.2900,6.1450],
[12.3000,6.1500],
[12.3100,6.1550],
[12.3200,6.1600],
[12.3300,6.1650],
[12.3400,6.1700],
[12.3500,6.1750],
[12.3600,6.1800],
[12.3700,6.1850],
[12.3800,6.1900],
[12.3900,6.1950],
[12.4000,6.2000],
[12.4100,6.2050],
[12.4200,6.2100],
[12.4300,6.2150],
[12.4400,6.2200],
[12.4500,6.2250],
[12.4600,6.2300],
[12.4700,6.2350],
[12.4800,6.2400],
[12.4900,6.2450],
[12.5000,6.2500],
[12.5100,6.2550],
[12.5200,6.2600],
[12.5300,6.2650],
[12.5400,6.2700],
[12.5500,6.2750],
[12.5600,6.2800],
[12.5700,6.2850],
[12.5800,6.2900],
[12.5900,6.2950],
[12.6000,6.3000],
[12.6100,6.3050],
[12.6200,6.3100],
[12.6300,6.3150],
[12.6400,6.3200],
[12.6500,6.3250],
[12.6600,6.3300],
[12.6700,6.3350],
[12.6800,6.3400],
[12.6900,6.3450],
[12.7000,6.3500],
[12.7100,6.3550],
[12.7200,6.3600],
[12.7300,6.3650],
[12.7400,6.3700],
[12.7500,6.3750],
[12.7600,6.3800],
[12.7700,6.3850],
[12.7800,6.3900],
[12.7900,6.3950],
[12.8000,6.4000],
[12.8100,6.4050],
[12.8200,6.4100],
[12.8300,6.4150],
[12.8400,6.4200],
[12.8500,6.4250],
[12.8600,6.4300],
[12.8700,6.4350],
[12.8800,6.4400],
[12.8900,6.4450],
[12.9000,6.4500],
[12.9100,6.4550],
[12.9200,6.4600],
[12.9300,6.4650],
[12.9400,6.4700],
[12.9500,6.4750],
[12.9600,6.4800],
[12.9700,6.4850],
[12.9800,6.4900],
[12.9900,6.4950],
[13.0000,6.5000],
[13.0100,6.5050],
[13.0200,6.5100],
[13.0300,6.5150],
[13.0400,6.5200],
[13.0500,6.5250],
[13.0600,6.5300],
[13.0700,6.5350],
[13.0800,6.5400],
[13.0900,6.5450],
[13.1000,6.5500],
[13.1100,6.5550],
[13.1200,6.5600],
[13.1300,6.5650],
[13.1400,6.5700],
[13.1500,6.5750],
[13.1600,6.5800],
[13.1700,6.5850],
[13.1800,6.5900],
[13.1900,6.5950],
[13.2000,6.6000],
[13.2100,6.6050],
[13.2200,6.6100],
[13.2300,6.6150],
[13.2400,6.6200],
[13.2500,6.6250],
[13.2600,6.6300],
[13.2700,6.6350],
[13.2800,6.6400],
[13.2900,6.6450],
[13.3000,6.6500],
[13.3100,6.6550],
[13.3200,6.6600],
[13.3300,6.6650],
[13.3400,6.6700],
[13.3500,6.6750],
[13.3600,6.6800],
[13.3700,6.6850],
[13.3800,6.6900],
[13.3900,6.6950],
[13.4000,6.7000],
[13.4100,6.7050],
[13.4200,6.7100],
[13.4300,6.7150],
[13.4400,6.7200],
[13.4500,6.7250],
[13.4600,6.7300],
[13.4700,6.7350],
[13.4800,6.7400],
[13.4900,6.7450],
[13.5000,6.7500],
[13.5100,6.7550],
[13.5200,6.7600],
[13.5300,6.7650],
[13.5400,6.7700],
[13.5500,6.7750],
[13.5600,6.7800],
[13.5700,6.7850],
[13.5800,6.7900],
[13.5900,6.7950],
[13.6000,6.8000],
[13.6100,6.8050],
[13.6200,6.8100],
[13.6300,6.8150],
[13.6400,6.8200],
[13.6500,6.8250],
[13.6600,6.8300],
[13.6700,6.8350],
[13.6800,6.8400],
[13.6900,6.8450],
[13.7000,6.8500],
[13.7100,6.8550],
[13.7200,6.8600],
[13.7300,6.8650],
[13.7400,6.8700],
[13.7500,6.8750],
[13.7600,6.8800],
[13.7700,6.8850],
[13.7800,6.8900],
[13.7900,6.8950],
[13.8000,6.9000],
[13.8100,6.9050],
[13.8200,6.9100],
[13.8300,6.9150],
[13.8400,6.9200],
[13.8500,6.9250],
[13.8600,6.9300],
[13.8700,6.9350],
[13.8800,6.9400],
[13.8900,6.9450],
[13.9000,6.9500],
[13.9100,6.9550],
[13.9200,6.9600],
[13.9300,6.9650],
[13.9400,6.9700],
[13.9500,6.9750],
[13.9600,6.9800],
[13.9700,6.9850],
[13.9800,6.9900],
[13.9900,6.9950],
[14.0000,7.0000],
[14.0100,7.0050],
[14.0200,7.0100],
[14.0300,7.0150],
[14.0400,7.0200],
[14.0500,7.0250],
[14.0600,7.0300],
[14.0700,7.0350],
[14.0800,7.0400],
[14.0900,7.0450],
[14.1000,7.0500],
[14.1100,7.0550],
[14.1200,7.0600],
[14.1300,7.0650],
[14.1400,7.0700],
[14.1500,7.0750],
[14.1600,7.0800],
[14.1700,7.0850],
[14.1800,7.0900],
[14.1900,7.0950],
[14.2000,7.1000],
[14.2100,7.1050],
[14.2200,7.1100],
[14.2300,7.1150],
[14.2400,7.1200],
[14.2500,7.1250],
[14.2600,7.1300],
[14.2700,7.1350],
[14.2800,7.1400],
[14.2900,7.1450],
[14.3000,7.1500],
[14.3100,7.1550],
[14.3200,7.1600],
[14.3300,7.1650],
[14.3400,7.1700],
[14.3500,7.1750],
[14.3600,7.1800],
[14.3700,7.1850],
[14.3800,7.1900],
[14.3900,7.1950],
[14.4000,7.2000],
[14.4100,7.2050],
[14.4200,7.2100],
[14.4300,7.2150],
[14.4400,7.2200],
[14.4500,7.2250],
[14.4600,7.2300],
[14.4700,7.2350],
[14.4800,7.2400],
[14.4900,7.2450],
[14.5000,7.2500],
[14.5100,7.2550],
[14.5200,7.2600],
[14.5300,7.2650],
[14.5400,7.2700],
[14.5500,7.2750],
[14.5600,7.2800],
[14.5700,7.2850],
[14.5800,7.2900],
[14.5900,7.2950],
[14.6000,7.3000],
[14.6100,7.3050],
[14.6200,7.3100],
[14.6300,7.3150],
[14.6400,7.3200],
[14.6500,7.3250],
[14.6600,7.3300],
[14.6700,7.3350],
[14.6800,7.3400],
[14.6900,7.3450],
[14.7000,7.3500],
[14.7100,7.3550],
[14.7200,7.3600],
[14.7300,7.3650],
[14.7400,7.3700],
[14.7500,7.3750],
[14.7600,7.3800],
[14.7700,7.3850],
[14.7800,7.3900],
[14.7900,7.3950],
[14.8000,7.4000],
[14.8100,7.4050],
[14.8200,7.4100],
[14.8300,7.4150],
[14.8400,7.4200],
[14.8500,7.4250],
[14.8600,7.4300],
[14.8700,7.4350],
[14.8800,7.4400],
[14.8900,7.4450],
[14.9000,7.4500],
[14.9100,7.4550],
[14.9200,7.4600],
[14.9300,7.4650],
[14.9400,7.4700],
[14.9500,7.4750],
[14.9600,7.4800],
[14.9700,7.4850],
[14.9800,7.4900],
[14.9900,7.4950],
[15.0000,7.5000],
[15.0100,7.5050],
[15.0200,7.5100],
[15.0300,7.5150],
[15.0400,7.5200],
[15.0500,7.5250],
[15.0600,7.5300],
[15.0700,7.5350],
[15.0800,7.5400],
[15.0900,7.5450],
[15.1000,7.5500],
[15.1100,7.5550],
[15.1200,7.5600],
[15.1300,7.5650],
[15.1400,7.5700],
[15.1500,7.5750],
[15.1600,7.5800],
[15.1700,7.5850],
[15.1800,7.5900],
[15.1900,7.5950],
[15.2000,7.6000],
[15.2100,7.6050],
[15.2200,7.6100],
[15.2300,7.6150],
[15.2400,7.6200],
[15.2500,7.6250],
[15.2600,7.6300],
[15.2700,7.6350],
[15.2800,7.6400],
[15.2900,7.6450],
[15.3000,7.6500],
[15.3100,7.6550],
[15.3200,7.6600],
[15.3300,7.6650],
[15.3400,7.6700],
[15.3500,7.6750],
[15.3600,7.6800],
[15.3700,7.6850],
[15.3800,7.6900],
[15.3900,7.6950],
[15.4000,7.7000],
[15.4100,7.7050],
[15.4200,7.7100],
[15.4300,7.7150],
[15.4400,7.7200],
[15.4500,7.7250],
[15.4600,7.7300],
[15.4700,7.7350],
[15.4800,7.7400],
[15.4900,7.7450],
[15.5000,7.7500],
[15.5100,7.7550],
[15.5200,7.7600],
[15.5300,7.7650],
[15.5400,7.7700],
[15.5500,7.7750],
[15.5600,7.7800],
[15.5700,7.7850],
[15.5800,7.7900],
[15.5900,7.7950],
[15.6000,7.8000],
[15.6100,7.8050],
[15.6200,7.8100],
[15.6300,7.8150],
[15.6400,7.8200],
[15.6500,7.8250],
[15.6600,7.8300],
[15.6700,7.8350],
[15.6800,7.8400],
[15.6900,7.8450],
[15.7000,7.8500],
[15.7100,7.8550],
[15.7200,7.8600],
[15.7300,7.8650],
[15.7400,7.8700],
[15.7500,7.8750],
[15.7600,7.8800],
[15.7700,7.8850],
[15.7800,7.8900],
[15.7900,7.8950],
[15.8000,7.9000],
[15.8100,7.9050],
[15.8200,7.9100],
[15.8300,7.9150],
[15.8400,7.9200],
[15.8500,7.9250],
[15.8600,7.9300],
[15.8700,7.9350],
[15.8800,7.9400],
[15.8900,7.9450],
[15.9000,7.9500],
[15.9100,7.9550],
[15.9200,7.9600],
[15.9300,7.9650],
[15.9400,7.9700],
[15.9500,7.9750],
[15.9600,7.9800],
[15.9700,7.9850],
[15.9800,7.9900],
[15.9900,7.9950],
[16.0000,8.0000],
[16.0100,8.0050],
[16.0200,8.0100],
[16.0300,8.0150],
[16.0400,8.0200],
[16.0500,8.0250],
[16.0600,8.0300],
[16.0700,8.0350],
[16.0800,8.0400],
[16.0900,8.0450],
[16.1000,8.0500],
[16.1100,8.0550],
[16.1200,8.0600],
[16.1300,8.0650],
[16.1400,8.0700],
[16.1500,8.0750],
[16.1600,8.0800],
[16.1700,8.0850],
[16.1800,8.0900],
[16.1900,8.0950],
[16.2000,8.1000],
[16.2100,8.1050],
[16.2200,8.1100],
[16.2300,8.1150],
[16.2400,8.1200],
[16.2500,8.1250],
[16.2600,8.1300],
[16.2700,8.1350],
[16.2800,8.1400],
[16.2900,8.1450],
[16.3000,8.1500],
[16.3100,8.1550],
[16.3200,8.1600],
[16.3300,8.1650],
[16.3400,8.1700],
[16.3500,8.1750],
[16.3600,8.1800],
[16.3700,8.1850],
[16.3800,8.1900],
[16.3900,8.1950],
[16.4000,8.2000],
[16.4100,8.2050],
[16.4200,8.2100],
[16.4300,8.2150],
[16.4400,8.2200],
[16.4500,8.2250],
[16.4600,8.2300],
[16.4700,8.2350],
[16.4800,8.2400],
[16.4900,8.2450],
[16.5000,8.2500],
[16.5100,8.2550],
[16.5200,8.2600],
[16.5300,8.2650],
[16.5400,8.2700],
[16.5500,8.2750],
[16.5600,8.2800],
[16.5700,8.2850],
[16.5800,8.2900],
[16.5900,8.2950],
[16.6000,8.3000],
[16.6100,8.3050],
[16.6200,8.3100],
[16.6300,8.3150],
[16.6400,8.3200],
[16.6500,8.3250],
[16.6600,8.3300],
[16.6700,8.3350],
[16.6800,8.3400],
[16.6900,8.3450],
[16.7000,8.3500],
[16.7100,8.3550],
[16.7200,8.3600],
[16.7300,8.3650],
[16.7400,8.3700],
[16.7500,8.3750],
[16.7600,8.3800],
[16.7700,8.3850],
[16.7800,8.3900],
[16.7900,8.3950],
[16.8000,8.4000],
[16.8100,8.4050],
[16.8200,8.4100],
[16.8300,8.4150],
[16.8400,8.4200],
[16.8500,8.4250],
[16.8600,8.4300],
[16.8700,8.4350],
[16.8800,8.4400],
[16.8900,8.4450],
[16.9000,8.4500],
[16.9100,8.4550],
[16.9200,8.4600],
[16.9300,8.4650],
[16.9400,8.4700],
[16.9500,8.4750],
[16.9600,8.4800],
[16.9700,8.4850],
[16.9800,8.4900],
[16.9900,8.4950],
[17.0000,8.5000],
[17.0100,8.5050],
[17.0200,8.5100],
[17.0300,8.5150],
[17.0400,8.5200],
[17.0500,8.5250],
[17.0600,8.5300],
[17.0700,8.5350],
[17.0800,8.5400],
[17.0900,8.5450],
[17.1000,8.5500],
[17.1100,8.5550],
[17.1200,8.5600],
[17.1300,8.5650],
[17.1400,8.5700],
[17.1500,8.5750],
[17.1600,8.5800],
[17.1700,8.5850],
[17.1800,8.5900],
[17.1900,8.5950],
[17.2000,8.6000],
[17.2100,8.6050],
[17.2200,8.6100],
[17.2300,8.6150],
[17.2400,8.6200],
[17.2500,8.6250],
[17.2600,8.6300],
[17.2700,8.6350],
[17.2800,8.6400],
[17.2900,8.6450],
[17.3000,8.6500],
[17.3100,8.6550],
[17.3200,8.6600],
[17.3300,8.6650],
[17.3400,8.6700],
[17.3500,8.6750],
[17.3600,8.6800],
[17.3700,8.6850],
[17.3800,8.6900],
[17.3900,8.6950],
[17.4000,8.7000],
[17.4100,8.7050],
[17.4200,8.7100],
[17.4300,8.7150],
[17.4400,8.7200],
[17.4500,8.7250],
[17.4600,8.7300],
[17.4700,8.7350],
[17.4800,8.7400],
[17.4900,8.7450],
[17.5000,8.7500],
[17.5100,8.7550],
[17.5200,8.7600],
[17.5300,8.7650],
[17.5400,8.7700],
[17.5500,8.7750],
[17.5600,8.7800],
[17.5700,8.7850],
[17.5800,8.7900],
[17.5900,8.7950],
[17.6000,8.8000],
[17.6100,8.8050],
[17.6200,8.8100],
[17.6300,8.8150],
[17.6400,8.8200],
[17.6500,8.8250],
[17.6600,8.8300],
[17.6700,8.8350],
[17.6800,8.8400],
[17.6900,8.8450],
[17.7000,8.8500],
[17.7100,8.8550],
[17.7200,8.8600],
[17.7300,8.8650],
[17.7400,8.8700],
[17.7500,8.8750],
[17.7600,8.8800],
[17.7700,8.8850],
[17.7800,8.8900],
[17.7900,8.8950],
[17.8000,8.9000],
[17.8100,8.9050],
[17.8200,8.9100],
[17.8300,8.9150],
[17.8400,8.9200],
[17.8500,8.9250],
[17.8600,8.9300],
[17.8700,8.9350],
[17.8800,8.9400],
[17.8900,8.9450],
[17.9000,8.9500],
[17.9100,8.9550],
[17.9200,8.9600],
[17.9300,8.9650],
[17.9400,8.9700],
[17.9500,8.9750],
[17.9600,8.9800],
[17.9700,8.9850],
[17.9800,8.9900],
[17.9900,8.9950],
[18.0000,9.0000],
[18.0100,9.0050],
[18.0200,9.0100],
[18.0300,9.0150],
[18.0400,9.0200],
[18.0500,9.0250],
[18.0600,9.0300],
[18.0700,9.0350],
[18.0800,9.0400],
[18.0900,9.0450],
[18.1000,9.0500],
[18.1100,9.0550],
[18.1200,9.0600],
[18.1300,9.0650],
[18.1400,9.0700],
[18.1500,9.0750],
[18.1600,9.0800],
[18.1700,9.0850],
[18.1800,9.0900],
[18.1900,9.0950],
[18.2000,9.1000],
[18.2100,9.1050],
[18.2200,9.1100],
[18.2300,9.1150],
[18.2400,9.1200],
[18.2500,9.1250],
[18.2600,9.1300],
[18.2700,9.1350],
[18.2800,9.1400],
[18.2900,9.1450],
[18.3000,9.1500],
[18.3100,9.1550],
[18.3200,9.1600],
[18.3300,9.1650],
[18.3400,9.1700],
[18.3500,9.1750],
[18.3600,9.1800],
[18.3700,9.1850],
[18.3800,9.1900],
[18.3900,9.1950],
[18.4000,9.2000],
[18.4100,9.2050],
[18.4200,9.2100],
[18.4300,9.2150],
[18.4400,9.2200],
[18.4500,9.2250],
[18.4600,9.2300],
[18.4700,9.2350],
[18.4800,9.2400],
[18.4900,9.2450],
[18.5000,9.2500],
[18.5100,9.2550],
[18.5200,9.2600],
[18.5300,9.2650],
[18.5400,9.2700],
[18.5500,9.2750],
[18.5600,9.2800],
[18.5700,9.2850],
[18.5800,9.2900],
[18.5900,9.2950],
[18.6000,9.3000],
[18.6100,9.3050],
[18.6200,9.3100],
[18.6300,9.3150],
[18.6400,9.3200],
[18.6500,9.3250],
[18.6600,9.3300],
[18.6700,9.3350],
[18.6800,9.3400],
[18.6900,9.3450],
[18.7000,9.3500],
[18.7100,9.3550],
[18.7200,9.3600],
[18.7300,9.3650],
[18.7400,9.3700],
[18.7500,9.3750],
[18.7600,9.3800],
[18.7700,9.3850],
[18.7800,9.3900],
[18.7900,9.3950],
[18.8000,9.4000],
[18.8100,9.4050],
[18.8200,9.4100],
[18.8300,9.4150],
[18.8400,9.4200],
[18.8500,9.4250],
[18.8600,9.4300],
[18.8700,9.4350],
[18.8800,9.4400],
[18.8900,9.4450],
[18.9000,9.4500],
[18.9100,9.4550],
[18.9200,9.4600],
[18.9300,9.4650],
[18.9400,9.4700],
[18.9500,9.4750],
[18.9600,9.4800],
[18.9700,9.4850],
[18.9800,9.4900],
[18.9900,9.4950],
[19.0000,9.5000],
[19.0100,9.5050],
[19.0200,9.5100],
[19.0300,9.5150],
[19.0400,9.5200],
[19.0500,9.5250],
[19.0600,9.5300],
[19.0700,9.5350],
[19.0800,9.5400],
[19.0900,9.5450],
[19.1000,9.5500],
[19.1100,9.5550],
[19.1200,9.5600],
[19.1300,9.5650],
[19.1400,9.5700],
[19.1500,9.5750],
[19.1600,9.5800],
[19.1700,9.5850],
[19.1800,9.5900],
[19.1900,9.5950],
[19.2000,9.6000],
[19.2100,9.6050],
[19.2200,9.6100],
[19.2300,9.6150],
[19.2400,9.6200],
[19.2500,9.6250],
[19.2600,9.6300],
[19.2700,9.6350],
[19.2800,9.6400],
[19.2900,9.6450],
[19.3000,9.6500],
[19.3100,9.6550],
[19.3200,9.6600],
[19.3300,9.6650],
[19.3400,9.6700],
[19.3500,9.6750],
[19.3600,9.6800],
[19.3700,9.6850],
[19.3800,9.6900],
[19.3900,9.6950],
[19.4000,9.7000],
[19.4100,9.7050],
[19.4200,9.7100],
[19.4300,9.7150],
[19.4400,9.7200],
[19.4500,9.7250],
[19.4600,9.7300],
[19.4700,9.7350],
[19.4800,9.7400],
[19.4900,9.7450],
[19.5000,9.7500],
[19.5100,9.7550],
[19.5200,9.7600],
[19.5300,9.7650],
[19.5400,9.7700],
[19.5500,9.7750],
[19.5600,9.7800],
[19.5700,9.7850],
[19.5800,9.7900],
[19.5900,9.7950],
[19.6000,9.8000],
[19.6100,9.8050],
[19.6200,9.8100],
[19.6300,9.8150],
[19.6400,9.8200],
[19.6500,9.8250],
[19.6600,9.8300],
[19.6700,9.8350],
[19.6800,9.8400],
[19.6900,9.8450],
[19.7000,9.8500],
[19.7100,9.8550],
[19.7200,9.8600],
[19.7300,9.8650],
[19.7400,9.8700],
[19.7500,9.8750],
[19.7600,9.8800],
[19.7700,9.8850],
[19.7800,9.8900],
[19.7900,9.8950],
[19.8000,9.9000],
[19.8100,9.9050],
[19.8200,9.9100],
[19.8300,9.9150],
[19.8400,9.9200],
[19.8500,9.9250],
[19.8600,9.9300],
[19.8700,9.9350],
[19.8800,9.9400],
[19.8900,9.9450],
[19.9000,9.9500],
[19.9100,9.9550],
[19.9200,9.9600],
[19.9300,9.9650],
[19.9400,9.9700],
[19.9500,9.9750],
[19.9600,9.9800],
[19.9700,9.9850],
[19.9800,9.9900],
[19.9900,9.9950],
[20.0000,10.0000],
[20.0100,10.0050],
[20.0200,10.0100],
[20.0300,10.0150],
[20.0400,10.0200],
[20.0500,10.0250],
[20.0600,10.0300],
[20.0700,10.0350],
[20.0800,10.0400],
[20.0900,10.0450],
[20.1000,10.0500],
[20.1100,10.0550],
[20.1200,10.0600],
[20.1300,10.0650],
[20.1400,10.0700],
[20.1500,10.0750],
[20.1600,10.0800],
[20.1700,10.0850],
[20.1800,10.0900],
[20.1900,10.0950],
[20.2000,10.1000],
[20.2100,10.1050],
[20.2200,10.1100],
[20.2300,10.1150],
[20.2400,10.1200],
[20.2500,10.1250],
[20.2600,10.1300],
[20.2700,10.1350],
[20.2800,10.1400],
[20.2900,10.1450],
[20.3000,10.1500],
[20.3100,10.1550],
[20.3200,10.1600],
[20.3300,10.1650],
[20.3400,10.1700],
[20.3500,10.1750],
[20.3600,10.1800],
[20.3700,10.1850],
[20.3800,10.1900],
[20.3900,10.1950],
[20.4000,10.2000],
[20.4100,10.2050],
[20.4200,10.2100],
[20.4300,10.2150],
[20.4400,10.2200],
[20.4500,10.2250],
[20.4600,10.2300],
[20.4700,10.2350],
[20.4800,10.2400],
[20.4900,10.2450],
[20.5000,10.2500],
[20.5100,10.2550],
[20.5200,10.2600],
[20.5300,10.2650],
[20.5400,10.2700],
[20.5500,10.2750],
[20.5600,10.2800],
[20.5700,10.2850],
[20.5800,10.2900],
[20.5900,10.2950],
[20.6000,10.3000],
[20.6100,10.3050],
[20.6200,10.3100],
[20.6300,10.3150],
[20.6400,10.3200],
[20.6500,10.3250],
[20.6600,10.3300],
[20.6700,10.3350],
[20.6800,10.3400],
[20.6900,10.3450],
[20.7000,10.3500],
[20.7100,10.3550],
[20.7200,10.3600],
[20.7300,10.3650],
[20.7400,10.3700],
[20.7500,10.3750],
[20.7600,10.3800],
[20.7700,10.3850],
[20.7800,10.3900],
[20.7900,10.3950],
[20.8000,10.4000],
[20.8100,10.4050],
[20.8200,10.4100],
[20.8300,10.4150],
[20.8400,10.4200],
[20.8500,10.4250],
[20.8600,10.4300],
[20.8700,10.4350],
[20.8800,10.4400],
[20.8900,10.4450],
[20.9000,10.4500],
[20.9100,10.4550],
[20.9200,10.4600],
[20.9300,10.4650],
[20.9400,10.4700],
[20.9500,10.4750],
[20.9600,10.4800],
[20.9700,10.4850],
[20.9800,10.4900],
[20.9900,10.4950],
[21.0000,10.5000],
[21.0100,10.5050],
[21.0200,10.5100],
[21.0300,10.5150],
[21.0400,10.5200],
[21.0500,10.5250],
[21.0600,10.5300],
[21.0700,10.5350],
[21.0800,10.5400],
[21.0900,10.5450],
[21.1000,10.5500],
[21.1100,10.5550],
[21.1200,10.5600],
[21.1300,10.5650],
[21.1400,10.5700],
[21.1500,10.5750],
[21.1600,10.5800],
[21.1700,10.5850],
[21.1800,10.5900],
[21.1900,10.5950],
[21.2000,10.6000],
[21.2100,10.6050],
[21.2200,10.6100],
[21.2300,10.6150],
[21.2400,10.6200],
[21.2500,10.6250],
[21.2600,10.6300],
[21.2700,10.6350],
[21.2800,10.6400],
[21.2900,10.6450],
[21.3000,10.6500],
[21.3100,10.6550],
[21.3200,10.6600],
[21.3300,10.6650],
[21.3400,10.6700],
[21.3500,10.6750],
[21.3600,10.6800],
[21.3700,10.6850],
[21.3800,10.6900],
[21.3900,10.6950],
[21.4000,10.7000],
[21.4100,10.7050],
[21.4200,10.7100],
[21.4300,10.7150],
[21.4400,10.7200],
[21.4500,10.7250],
[21.4600,10.7300],
[21.4700,10.7350],
[21.4800,10.7400],
[21.4900,10.7450],
[21.5000,10.7500],
[21.5100,10.7550],
[21.5200,10.7600],
[21.5300,10.7650],
[21.5400,10.7700],
[21.5500,10.7750],
[21.5600,10.7800],
[21.5700,10.7850],
[21.5800,10.7900],
[21.5900,10.7950],
[21.6000,10.8000],
[21.6100,10.8050],
[21.6200,10.8100],
[21.6300,10.8150],
[21.6400,10.8200],
[21.6500,10.8250],
[21.6600,10.8300],
[21.6700,10.8350],
[21.6800,10.8400],
[21.6900,10.8450],
[21.7000,10.8500],
[21.7100,10.8550],
[21.7200,10.8600],
[21.7300,10.8650],
[21.7400,10.8700],
[21.7500,10.8750],
[21.7600,10.8800],
[21.7700,10.8850],
[21.7800,10.8900],
[21.7900,10.8950],
[21.8000,10.9000],
[21.8100,10.9050],
[21.8200,10.9100],
[21.8300,10.9150],
[21.8400,10.9200],
[21.8500,10.9250],
[21.8600,10.9300],
[21.8700,10.9350],
[21.8800,10.9400],
[21.8900,10.9450],
[21.9000,10.9500],
[21.9100,10.9550],
[21.9200,10.9600],
[21.9300,10.9650],
[21.9400,10.9700],
[21.9500,10.9750],
[21.9600,10.9800],
[21.9700,10.9850],
[21.9800,10.9900],
[21.9900,10.9950],
[22.0000,11.0000]]
)