package main

import (
	"Modul5_Tugas/controller"
	"fmt"
	"log"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
	"github.com/gorilla/mux"
)

func main() {
	aarouter := mux.NewRouter()
	// router.HandleFunc("/users", controller.GetAllUsers).Methods("GET")
	router.HandleFunc("/products", controller.GetAllProducts).Methods("GET")
	router.HandleFunc("/transactions", controller.GetAllTransactions).Methods("GET")
	router.HandleFunc("/users", controller.InsertUser).Methods("POST")
	// router.HandleFunc("/products", controller.InsertProduct).Methods("POST")
	router.HandleFunc("/transactions", controller.InsertTransaction).Methods("POST")
	// router.HandleFunc("/users", controller.DeleteUser).Methods("DELETE")
	router.HandleFunc("/products", controller.DeleteProduct).Methods("DELETE")
	router.HandleFunc("/transactions", controller.DeleteTransaction).Methods("DELETE")
	// router.HandleFunc("/users", controller.UpdateUser).Methods("PUT")
	router.HandleFunc("/products", controller.UpdateProduct).Methods("PUT")
	router.HandleFunc("/transactions", controller.UpdateTransaction).Methods("PUT")
	router.HandleFunc("/detail_address", controller.GetUserAddresses).Methods("GET")
	router.HandleFunc("/detail_product", controller.GetUserProducts).Methods("GET")
	// router.HandleFunc("/detail_transaction", controller.GetUserDetailTransactions).Methods("GET")
	router.HandleFunc("/detail_transaction", controller.GetUserDetailTransactionByID).Methods("GET")
	// router.HandleFunc("/users", controller.LoginUser).Methods("GET")
	router.HandleFunc("/products", controller.InsertProducts).Methods("POST")
	router.HandleFunc("/users", controller.UpdateUsers).Methods("PUT")
	router.HandleFunc("/users", controller.DeleteUsers).Methods("DELETE")
	// router.HandleFunc("/users", controller.GetAllUsersUsingGorm).Methods("GET")
	router.HandleFunc("/users", controller.GetUserByID).Methods("GET")

	http.Handle("/", router)
	fmt.Println("Connected to Port 8080")
	log.Println("Connected to Port 8080")
	log.Fatal(http.ListenAndServe(":8080", router))
}
