export interface Product {
  id: string;
  name: string;
  model: string;
  category: string;
  brand: string;
  images: string[];
  price: number | string;
  short_description: string;
  long_description: string;
  docs: {
    name: string;
    url: string;
  }[];
}
