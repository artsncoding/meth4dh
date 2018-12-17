import React, { Component } from 'react';
import './App.css';

class ImageWindow extends Component{
  constructor(props){
    super(props)
  }
    render(){
    const {image} = this.props;
    return(
      <div id="imageWindow">
      <p>here come the images{image}</p>
      </div>
    )
    }
  }

  class Buttons extends Component {
    render(){
      return(
        <div id="buttonPanel">
          <button></button>
        </div>
      )
    }

  }

class App extends Component {
  constructor(props){
    super(props)
    this.state={
      imageId: 0,
    }
  }

  render() {
    return (
      <div className="App">
        <h1>Methods for Digital Humanities</h1>
        <ImageWindow
          image ="hi"
        />
        <div>
          <button>Home</button>
          <button>Map</button>
          <button>Timeline</button>
          <button>3rd Visualization</button>
        </div>
      </div>
    );
  }
}

export default App;
