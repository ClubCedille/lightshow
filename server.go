package main

/*
* Name : server.go
* Author : Nicolas De Oliveira Nadeau
*	Description : small UDP server, listen on a specific port for a connection
* 							data and do what he have to do ! (LIGHTSHOW!)
* Next Step : GPIO, lib also working in go! so next step is to make it work
 */
import (
	"fmt"
	"net"
	"os"
	"github.com/stianeikeland/go-rpio"
)

var (
	pin11 = rpio.Pin(17)
        pin13 = rpio.Pin(27)
        pin15 = rpio.Pin(22)
)


/* A Simple function to verify error */
func CheckError(err error) {
	if err != nil {
		fmt.Println("Error: ", err)
		os.Exit(0)
	}
}

/*
*	Main program !
* Server Side
*
 */
func main() {


	rpio.Open();
	

	/* Lets prepare a address at any address at port 10001*/
	ServerAddr, err := net.ResolveUDPAddr("udp", ":10001")
	CheckError(err)

	/* Now listen at selected port */
	ServerConn, err := net.ListenUDP("udp", ServerAddr)
	CheckError(err)
	defer ServerConn.Close()

	buf := make([]byte, 1024)

	for {
		n, addr, err := ServerConn.ReadFromUDP(buf)
		fmt.Println("Received", string(buf[0:n]), "from", addr)

		if string(buf[0:n]) == "00" {
			fmt.Println("No face")
			faceLightDown()
		}
		if string(buf[0:n]) == "01" {
			fmt.Println("Face")
			faceLightUp()
		}
		if string(buf[0:n]) == "10" {
			fmt.Println("No eyes")
			eyeLightDown()
		}
		if string(buf[0:n]) == "11" {
			fmt.Println("Eyes")
			eyeLightUp()
		}

		if err != nil {
			fmt.Println("Error: ", err)
		}
	}
}

func faceLightUp() {
	//pin11.PullLow()

	pin11.Output() 
	pin11.High()
}
func faceLightDown() {
	pin11.Low()
	pin11.PullDown()
}
func eyeLightUp() {
	//pin13.PullLow()
	//pin15.PullLow()

	pin13.Output()
	pin15.Output()  
	
	pin13.High()
	pin15.High()
}
func eyeLightDown() {
	pin13.Low()
	pin15.Low()  

	pin13.PullDown()
	pin15.PullDown()
}

