import { Container } from "react-bootstrap"

export default function About() {
    return (
        <main className="my-5 py-5">
            <Container className="px-0">
                <h1>Launch a business compaign</h1>

                    <textarea class="form-control" rows="5" id="comment" name="text" placeholder="I want to ... "></textarea>
                    <button>Next</button>
            </Container>
        </main>
            )
}