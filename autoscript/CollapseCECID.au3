#cs ----------------------------------------------------------------------------

 AutoIt Version: 3.3.8.1
 Author:         Summer

 Script Function:
	Expand all tree by an cecid
#ce ----------------------------------------------------------------------------

#include <IE.au3>
#include <debug.au3>

_DebugSetup("Log")
$oIE = _IECreate("http://wwwin-tools.cisco.com/dir/details/jianbfan")
_DebugOut(@error)
WinSetState("[CLASS:IEFrame]","",@SW_MAXIMIZE)
_IELoadWait($oIE)
Sleep(3000)

Local $sMyString = "Reporting Structure"
;Local $oLinks = _IELinkGetCollection($oIE, -1)
Local $oLinks = $oIE.document.links
Local $i = $oLinks.length
_DebugOut($i)

For $oLink In $oLinks
    Local $sLinkText = _IEPropertyGet($oLink, "innerText")
    If StringInStr($sLinkText, $sMyString) Then
        _IEAction($oLink, "click")
        ExitLoop
    EndIf
Next

_IELoadWait($oIE)

Do
	Local  $imgs = $oIE.document.images
	For $img In $imgs
		If $img.src == "http://wwwin.cisco.com/cec/common/i/icon_plus.gif" Then
			$img.click()
		EndIf
	Next
	Sleep(2000) ;If it doesn't sleep, it will cause the mistake in next loop.
Until (bPlusNotExist($oIE))

Func bPlusNotExist(ByRef $oIE)
 	Local $i = 0;
 	Local $imgs = $oIE.document.images
	For $img In $imgs
		If $img.src == "http://wwwin.cisco.com/cec/common/i/icon_plus.gif" Then
			$i=$i + 1
;~ 			if $i >= 2 Then ;Even all + is expanded, there are still one + icon.
;~ 				ExitLoop
;~ 			EndIf
		EndIf
	Next
;	_DebugOut("bIsPlusExist:" & $i)
	if 1 == $i Then
		Return True
	Else
		Return False
	EndIf
EndFunc