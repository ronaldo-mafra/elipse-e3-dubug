Sub logAndDebug_onEventError()
	if DocString <> "" then
		' arg = [log type (int), msg (string)]
		' arg(0) --> 0 info [+], 1 warning [!], 2 error [-], 3 DEBUG terminal (implementação em python)
		' passada pela docString da tag, separado por ";"
		symbol		= array("[+] ","[!] ","[-] ")
		enbDebug 	= true
		arg 		= split(DocString, ";")
		pathLog 	= "C:\PRO_VLA\sysLog\"
		logName 	= Split(Now()," ")
		outFile 	= pathLog & Replace(logName(0), "/", "-") & ".txt"
		dataFile	= ""
		Set obj = CreateObject("Scripting.FileSystemObject").OpenTextFile(outFile,8,true)

		if arg(0) < 3 then
			dataFile = symbol(arg(0)) & now()& " - " & arg(1)
			obj.WriteLine(dataFile)
			obj.Close
		elseif arg(0) = 3 then
			debug arg(1), enbDebug
		end if

		DocString 	= ""
	end if

end sub
Sub debug(msg, enableDebug)
	if enableDebug then
		set pyDebug = CreateObject("WSCript.shell")
		pyDebug.run ".\elipseE3Debug\e3DebugCli.py 4444 """& msg & """",0,True
	End If
End Sub

Sub a()
End Sub