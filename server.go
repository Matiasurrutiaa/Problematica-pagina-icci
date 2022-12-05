package main

import "github.com/gin-gonic/gin"

func main() {
	router := gin.Default()

	router.GET("/:param?query=Matias", func(c *gin.Context) {
		param := c.Param("param")
		query := c.Query("param")

		cadena := "Parametro: " + param + "Query: " + query

		c.JSON(200, cadena)
	})

	router.POST("/", func(c *gin.Context) {
		c.JSON(200, "POST")

	})

	router.PUT("/", func(c *gin.Context) {
		c.JSON(200, "PUT")
	})

	router.DELETE("/", func(c *gin.Context) {
		c.JSON(200, "DELETE")
	})

	router.Run(":4001")

}
