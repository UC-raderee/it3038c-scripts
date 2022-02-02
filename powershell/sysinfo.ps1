function getIP{ 

    (get-netipaddress).ipv4address | Select-String "192*" 

} 
write-host(getIP) 
$IP = getIP

function GetVersion{ 

    Get-Host | Select-Object Version 

} 
write-host(GetVersion) 
$Version = GetVersion

function GetDate{ 

    Get-Date 

} 
write-host(GetDate) 
$Date = GetDate


Send-MailMessage -To "leonardf@ucmail.uc.edu" -From "erader27@gmail.com" -Subject "IT3038C Windows SysInfo" -Body "My IP Address is: $IP. User is $env:USERNAME. Hostname is $env:computername. Powershell version is $Version. Today is $Date.  Yes I did this at 4:00 a.m., please don't judge me. Having issues pushing to GitHub but I'll ask in class.  Woohoo for Sandbox working!" -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential) 