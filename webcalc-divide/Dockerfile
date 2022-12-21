FROM golang:latest

RUN mkdir -p /app

WORKDIR /app

ADD /src /app

RUN go build ./main.go

EXPOSE 6000

CMD ["./main"]
