@echo off
CALL "..\simc.exe" "GenericOptions.simc" "..\..\Dump\Input\Base\Arcane.simc" "..\..\Dump\Input\Talents\Talents_Arcane.simc"
MOVE /Y "output.txt" "D:\SimC Scripts\Dump\Output\Talents\ST\Arcane.txt"
CALL "..\simc.exe" "GenericOptions.simc" "..\..\Dump\Input\Base\Fire.simc" "..\..\Dump\Input\Talents\Talents_Fire.simc"
MOVE /Y "output.txt" "D:\SimC Scripts\Dump\Output\Talents\ST\Fire.txt"
CALL "..\simc.exe" "GenericOptions.simc" "..\..\Dump\Input\Base\Frost.simc" "..\..\Dump\Input\Talents\Talents_Frost.simc"
MOVE /Y "output.txt" "D:\SimC Scripts\Dump\Output\Talents\ST\Frost.txt"