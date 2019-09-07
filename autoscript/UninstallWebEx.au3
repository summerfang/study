#include <MsgBoxConstants.au3>
#include <StringConstants.au3>
#include <Debug.au3>

_DebugSetup("Uninstall WebEx", True);

UninstallWebEx();

Func UninstallWebEx()
   Local $sSubKey = "";

   Local $i = 0, $iErr = 0;
   Do
	  $i = $i + 1;
	  $sSubKey = RegEnumKey(GetWebExUnstallDirectory() & "", $i);
	  $iErr = @error;
	  if 0 == $iErr Then
		 Local $sProductCodeRegPath = GetWebExUnstallDirectory() & $sSubKey & "\";
		 Local $sPublisher = RegRead($sProductCodeRegPath, "Publisher");

		 if "Cisco WebEx LLC" == $sPublisher Then
			Local $sDisplayName = RegRead($sProductCodeRegPath, "DisplayName");
			Local $sUninstallString = RegRead($sProductCodeRegPath, "UninstallString");
			if 0 == @error Then
			   if StringInStr($sUninstallString, "atcliun.exe") Then
				  RunWait($sUninstallString);
				  ContinueLoop;
			   EndIf
			   Local $aProductCode = StringRegExp($sUninstallString, "\{([^\{^\}]*)\}", $STR_REGEXPARRAYFULLMATCH);
			   if 0 == @error Then
				  Local $sSlientUninstallCMD = "MsiExec.exe /X" & $aProductCode[0] & " /quiet /norestart";
				  _DebugOut("Uninstall" & " " & $sDisplayName & ": " & $sSlientUninstallCMD & "...", 2);
				  RunWait($sSlientUninstallCMD);
			   EndIf
			EndIf
		 EndIf
	  EndIf
   Until $iErr <> 0
EndFunc

Func GetWebExUnstallDirectory()
   Local $sUninstallDirectory32 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\";
   Local $sUninstallDirectory32on64 = "HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\";

   Local $sUninstallDirectory;

   if "X86" == @OSArch Then
	  $sUninstallDirectory = $sUninstallDirectory32;
   Else
	  $sUninstallDirectory = $sUninstallDirectory32on64;
   EndIf
   Return $sUninstallDirectory
EndFunc