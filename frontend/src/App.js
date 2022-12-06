import logo from './logo.svg';
import './App.css';
import React from "react";

let productData = [
  {
    id: "1",
    nome: "Moletom",
    descricao: "Moletom do CAM",
    imagem_url: "https://img.youcom.com.br/Custom/Content/Products/10/90/1090480_moletom-canguru-liso_l32_637927046348070606.jpg",
    valor: "100",
    valor_com_desconto: "3",
    desconto: "True",
    ativo: "True",
    quantidade: "4",
    tamanho: "M",
  },
  {
    id: "2",
    nome: "Moletom",
    descricao: "Moletom do CAM",
    imagem_url: "https://img.youcom.com.br/Custom/Content/Products/10/90/1090480_moletom-canguru-liso_l32_637927046348070606.jpg",
    valor: "100",
    valor_com_desconto: "3",
    desconto: "True",
    ativo: "True",
    quantidade: "4",
    tamanho: "M",
  },
  {
    id: "3",
    nome: "Moletom",
    descricao: "Moletom do CAM",
    imagem_url: "https://img.youcom.com.br/Custom/Content/Products/10/90/1090480_moletom-canguru-liso_l32_637927046348070606.jpg",
    valor: "100",
    valor_com_desconto: "3",
    desconto: "True",
    ativo: "True",
    quantidade: "4",
    tamanho: "M",
  }
];




function ProductsTable(props) {
  const { list, onDismiss, searchTerm} = props;
  return (
      <table>
        <thead>
          <tr>
            <th>Id</th>
            <th>Nome do Produto</th>
            <th>Descricao</th>
            <th>Valor</th>
          </tr>
        </thead>
        <tbody>
          {list.filter(product => product.nome.toLowerCase().includes(searchTerm.toLowerCase()))
          .map((product) => (
            <tr key={product.id}>
              <td>{product.id}</td>
              <td>{product.nome}</td>
              <td>{product.descricao}</td>
              <td>{product.valor}</td>
              <td>
                <Button onClick={() => onDismiss(product.id)}>Dismiss</Button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
  );
}

function Search(props) {
  const {searchTerm, handleInputChange} = props;
  return (
      <form>
        <input type="text" placeholder="Search by product name"
          name="searchTerm"
          value={searchTerm} 
          onChange={(event) => handleInputChange(event)}/>
      </form>
    );
}

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { list: null };
  }
  handleInputChange(event) {
    const target = event.target;
    const value = 
      target.type === 'checkbox' ? target.checked : target.value;
    const name = target.name;

    this.setState({
      [name]: value
    });
  }
  onSearchChange(event) {
    this.setState({ searchTerm: event.target.value });
  }
  onDismiss(id) {
    const updatedList = this.state.list.filter(item => item.id !== id);
    this.setState({ list: updatedList });
  }

  componentDidMount() {
    fetch('http://127.0.0.1:8000/api/v1/products/')
      .then((response) => response.json())
      .then((result) => this.setState({ list: result }))
      .catch((error) => error);
  }
  render() {
      const {list, searchTerm} = this.state;
      
      return (
        <div className="App">
          <Search
            searchTerm={searchTerm}
            handleInputChange={(e) => this.handleInputChange(e)}
          >
            Search term:
          </Search>
          <ProductsTable list={list} 
            onDismiss={(id) => this.onDismiss(id)}
            searchTerm={searchTerm}
            onSearchChange={(e) => this.onSearchChange(e)}
          />
      </div>
    );
  }
}
function Button(props) {
  const {
    onClick,
    className='',
    children,
  } = props;

  return (
    <button
      onClick={onClick}
      className={className}
      type="button"
    >
      {children}
    </button>
  );
}

export default App;
