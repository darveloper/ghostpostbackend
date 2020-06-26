class App extends Component {
    constructor(props) {
      super(props);
      this.state = {
        posts: [],
        loaded: false,
        placeholder: "Loading"
      };
    }
  
    componentDidMount() {
      fetch("http://127.0.0.1:8000/posts/")
        .then(response => {
          if (response.status > 400) {
            return this.setState(() => {
              return { placeholder: "Something went wrong!" };
            });
          }
          return response.json();
        })
        .then(posts => {
          this.setState(() => {
            return {
              posts,
              loaded: true
            };
          });
        });
    }
  
    render() {
      return (
        <ul>
          {this.state.posts.map(post => {
            return (
              <div key={post.id}>
                {post.text} - {post.time}
              </div>
            );
          })}
        </ul>
      );
    }
  }
  
  export default App;
  
  const container = document.getElementById("app");
  render(<App />, container);