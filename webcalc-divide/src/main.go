package main

//Relevant imports
import (
  "encoding/json"
  "net/http"
  "fmt"
  "strconv"
)

//Building a struct to then be converted to json for return
type ReturnType struct {
  Answer string `json:"answer"`
  Formula string `json:"string"`
  Error string `json:"error"`
}

//Main entry point, sends request to functionHandler
func main() {
  http.HandleFunc("/",funcHandler)
  http.HandleFunc("/hi",testHandler)
  http.ListenAndServe(":6000", nil)

}

func testHandler(w http.ResponseWriter, req *http.Request) {
  fmt.Fprintf(w, "Hello, %s!", req.URL.Path[1:])
}

//Parses X and Y out of request, converts to integer with respect to error.
//If X and Y both int, pass into divide num, create an instance of ReturnType
//struct and encode into JSON format and return.
func funcHandler(w http.ResponseWriter, req *http.Request) {

  w.Header().Set("Content-Type", "application/json")
  w.Header().Set("Access-Control-Allow-Origin", "*")

  XVal := req.FormValue("x")
  YVal := req.FormValue("y")

//Basic check to ensure X and Y values are filled.

  x, err1 := strconv.Atoi(XVal)
  y, err2 := strconv.Atoi(YVal)


  if err1 == nil && err2 == nil {
    if y == 0 {
      returnAns := "undefined"
      returnFormula := XVal + "/" + YVal + "= Undefined"
      r := ReturnType{returnAns, returnFormula, "true - Cannot divide by 0"}
      json.NewEncoder(w).Encode(r)
    } else {
      ans := dividenum(x,y)
      returnAns := strconv.Itoa(ans)
      returnFormula := XVal + "/" + YVal + "=" + returnAns
      r := ReturnType{returnAns, returnFormula, "false"}
      json.NewEncoder(w).Encode(r)
    }

  } else {
    returnAns := "Undefined"
    returnFormula := "Error - Invalid parameters"
    r := ReturnType{returnAns, returnFormula, "true"}
    json.NewEncoder(w).Encode(r)
  }


}

//Basic divide number function
func dividenum(x int, y int) int {
  return x/y
}
