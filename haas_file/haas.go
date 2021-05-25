package main


import (

    "log"
    "os"
    "os/exec"
)


func main() {

    cmd := exec.Command("/home/haasm/scripts/haas_file/haasv01.py")
    cmd.Stdout = os.Stdout
    cmd.Stderr = os.Stderr
    log.Println(cmd.Run())

}
