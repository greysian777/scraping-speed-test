package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strings"
	"time"

	"github.com/gocolly/colly"
	"github.com/pkg/profile"
)

func main() {
	defer profile.Start().Stop()
	content, _ := ioutil.ReadFile("test_links.txt")
	tempLink := strings.Split(string(content), "\n")
	var linkArray []string
	for _, link := range tempLink {
		if link != "" {
			linkArray = append(linkArray, link)
		}
	}

	var pages []string
	c := colly.NewCollector(colly.Async())
	//c.Limit(&colly.LimitRule{DomainGlob: "*", Parallelism: 2})

	c.OnHTML("div[class=read__content]", func(e *colly.HTMLElement) {
		pages = append(pages, e.ChildText("p"))
	})
	// c.OnRequest(func(r *colly.Request) {
	// 	log.Println("Visiting", r.URL)
	// })
	start := time.Now()
	for _, link := range linkArray {
		c.Visit(link)
	}
	//c.Wait()
	end := time.Now()
	elapsed := end.Sub(start)
	fmt.Println(pages)
	log.Println(elapsed)
}
