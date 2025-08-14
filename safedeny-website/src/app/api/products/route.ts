import { NextResponse } from 'next/server';
import products from '@/data/products.json';

export async function GET(request: Request) {
  // In a real application, you might add logic for pagination, filtering, etc.
  // For now, we just return the whole list.
  return NextResponse.json(products);
}
