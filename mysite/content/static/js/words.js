import React from 'react';
import ReactDOM from 'react-dom';
import {Modal, Buttton} from 'bootstrap-react';


class WordAdd extends React.Component {

}



class WordGroup extends React.Component {
  constructor(props) {
    super(props);
    this.state = {showModal: false};

    this.openModal = this.openModal.bind(this);
    this.closeModal = this.closeModal.bind(this);
  }

  openModal() {
    this.setState({showModal: true});
  }

  closeModal() {
    this.setState({showModal: false});
  }

  wordMap () {
    /* Not enitrely sure about this here.

    const words = this.props.words;
    const listWords = words.map((word) =>
      <WordItem value={}>
  )*/
  }

  render() {
    return (
      <div>
      <h2>React-Bootstrap is not working</h2>
        <Button bsStyle="primary" onClick={this.openModal}> + </Button>
      </div>
    );
  }
}

ReactDOM.render(<WordGroup />, document.getElementById('words'));
