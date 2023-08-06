package main

import (
	"crypto/rand"
	"github.com/pedroalbanese/gogost/v5/gost3410"
	"github.com/pedroalbanese/v5/gost34112012256"
	"io"
)

func main() {
	data := []byte("data to be signed")
	hasher := gost34112012256.New()
	_, err := hasher.Write(data)
	dgst := hasher.Sum(nil)
	curve := gost3410.CurveIdtc26gost341012256paramSetB()
	prvRaw := make([]byte, 32)
	_, err = io.ReadFull(rand.Reader, prvRaw)
	prv, err := gost3410.NewPrivateKey(curve, prvRaw)
	pub, err := prv.PublicKey()
	pubRaw := pub.Raw()
	sign, err := prv.Sign(rand.Reader, dgst, nil)
	pub, err = gost3410.NewPublicKey(curve, pubRaw)
	isValid, err := pub.VerifyDigest(dgst, sign)
	if !isValid {
		panic("signature is invalid")
	}
}
