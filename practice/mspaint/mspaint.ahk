#Warn All
Process, Close, mspaint.exe
pasta_entrada := "entrada\*.txt"
pasta_processando := "processando"
pasta_finalizado := "finalizado"

; Loop pasta de entrada até encontrar .txt

; Mover arquivos .txt para pasta de processamento
FileMove, % pasta_entrada, % pasta_processando
Sleep 1000

Loop, Files, % pasta_processando . "\*.txt"
{
    agora := A_Now
    FileRead, OutputVar, % A_LoopFileFullPath
    
    ; Capturar informações na pasta de processamento
    infos := StrSplit(OutputVar, ";")
    forma := % infos[1]
    cor :=  % infos[2]
    
    Run mspaint
    WinWaitActive, ahk_exe mspaint.exe,, 3
    
    valida_forma := % A_WorkingDir . "\valida\" . forma . ".png"
    Send, {Alt}"hsh" ; atalho para formas
    Sleep, 500
    ImageSearch, x, y, 0, 0, % A_ScreenWidth, % A_ScreenHeight, % valida_forma
    
    if (not x)
    {
        MsgBox, Deu ruim.
        ExitApp
    }
    
    MouseClick, L, % x + 10 , % y + 10
    ;ExitApp
    /* Switch % forma
    {
    Case "circulo":
        Send, {Right}{Right}{Enter}                                     ; circulo
    Case "retangulo":
        Send, {Right}{Right}{Right}{Enter}                              ; retangulo
    Case "triangulo":
        Send, {Right}{Right}{Right}{Right}{Right}{Right}{Enter}         ; triangulo
    }
    */   
        
    Sleep, 250  
    Send, {Alt}"hi"                             ; preencher forma
    Sleep, 250
    Send, {Down}{Enter}                         ; cor sólida
    Sleep, 250
    Send, {Alt}"h2"                             ; escolher cor 2 (preenchimento)

    Switch % cor
    {
    Case "amarelo":
        MouseClick L, 995, 70       ; coord funcionam apenas com a janela maximizada
    Case "azul":
        MouseClick L, 1035, 70
    Case "vermelho":
        MouseClick L, 950, 70
    }

    ; desenhar a forma
    MouseClickDrag, L, 20, 160, 120, 260
    MouseClick, L, 200, 400
    Sleep, 250
    
    valida_desenho := % A_WorkingDir . "\valida\" . forma . "_" . cor . ".png"
    ImageSearch, x, y, 0, 0, % A_ScreenWidth, % A_ScreenHeight, % valida_desenho

    if (x)
    {
        ; salvar arquivo
        FormatTime, pasta_output, % agora, yyyy-MM-dd HH-mm-ss
        
        new_dir := % A_WorkingDir . "\" . pasta_finalizado . "\" . pasta_output 
        new_file_name := % new_dir . "\" . forma . "_" . cor . ".png"
        
        FileCreateDir % new_dir
        Send, {F12}
        WinWaitActive Salvar como,, 3
        ControlFocus, Edit1
        Sleep, 1000
        Clipboard := new_file_name
        Send, ^{v}
        Sleep, 500
        ControlFocus Button2
        Send, {Space}
        Sleep, 1000
        Process, Close, mspaint.exe

        ; mover arquivo .txt
        FileMove, % A_LoopFileFullPath, % new_dir . "\" . A_LoopFileName
        Sleep, 1000
    }

    ;Break
}
ExitApp
F10::ExitApp