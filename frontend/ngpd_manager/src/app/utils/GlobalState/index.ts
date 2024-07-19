class GlobalState {
    private value: Record<string, string> = {};
  
    getValue(key: string) {
      return this.value[key];
    }
  
    setValue(key: string, value: string) {
      this.value[key] = value;
    }
  }
  const globalState = new GlobalState();
  export default globalState;