
------------------------------------------------- elipseE3Debug v0.1 -------------------------------------------------

1 - Instalar o compilador python3.7
2 - Executar o "e3DebugTools.py"

Para teste executar no terminal [e3DebugCli.py "Teste msg"] e verificar se a msg aparece 
no terminal do "e3DebugTools.py"

Uso do debug no elipse E3:
	No evendo inserir a Sub "debug"
	
	Chadada do debug
		debug("[DEBUG] (*String)")

Obs.:
	a pasta "elipseE3Debug" deve ficar na raiz do projeto do supervisorio.

-----------------------------------------------------------------------------------------------------------------------

#######################################################################################

End Sub

Sub debug(msg)
	set pyDebug = CreateObject("WSCript.shell")
	pyDebug.run ".\elipseE3Debug\e3DebugCli.py [PORT] """& msg & """",0,True
End Sub

Sub a()

#######################################################################################
# elipse-e3-dubug
