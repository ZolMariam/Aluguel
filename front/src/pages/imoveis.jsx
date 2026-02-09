import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Imoveis = () => {
  const [imoveis, setImoveis] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get('http://localhost:8000/api/imoveis')
      .then(response => {
        setImoveis(response.data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Erro ao buscar usuários:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Carregando imoveis...</p>;
  }

  return (
    <div style={{ padding: '20px' }}>
      <h2>Lista de Imoveis</h2>

      <table border="1" cellPadding="10" cellSpacing="0">
        <thead>
          <tr>
            <th>ID</th>
            <th>Titulo</th>
            <th>Valor</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {imoveis.map(imovel => (
            <tr key={imovel.id}>
              <td>{imovel.id}</td>
              <td>{imovel.titulo}</td>
              <td>{imovel.valor_aluguel}</td>
              <td>{imovel.status}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Imoveis;
