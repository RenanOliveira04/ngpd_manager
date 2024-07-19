interface Pessoa {
    nome: string;
    email: string;
    cargo: string;
  }
  
  interface Aluno extends Omit<Pessoa, "cargo"> {}
  
  interface Professor extends Pick<Pessoa, "nome"> {}
  
  export type { Pessoa, Aluno, Professor };