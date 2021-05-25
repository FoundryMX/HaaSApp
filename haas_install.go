package main


import (

    "log"
    "os"
   // "os/exec"
)


func main() {

    if _, err := os.Stat("~/haas_app/haas"); err != nil {
		if os.IsNotExist(err) {
			log.Println("file does not exist")
			err1 := os.Mkdir("~/haas_app", 0755)
			if err1 != nil {
				log.Fatal(err1)
			}
			//cmd := exec.Command("mkdir haas_app")
			// file does not exist
		} else {
			log.Println("file exists")

			// other error
		}
	}
	
	


    //cmd.Stdout = os.Stdout
    //cmd.Stderr = os.Stderr
    //log.Println(cmd.Run())

}
