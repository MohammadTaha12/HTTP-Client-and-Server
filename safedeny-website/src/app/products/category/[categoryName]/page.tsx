import Link from 'next/link';
import Image from 'next/image';
import { Product } from '@/types';

async function getProducts(): Promise<Product[]> {
  const baseUrl = process.env.VERCEL_URL ? `https://${process.env.VERCEL_URL}` : 'http://localhost:3000';
  const res = await fetch(`${baseUrl}/api/products`, { cache: 'no-store' });
  if (!res.ok) {
    throw new Error('Failed to fetch products');
  }
  return res.json();
}

interface CategoryPageProps {
  params: {
    categoryName: string;
  };
}

export default async function CategoryPage({ params }: CategoryPageProps) {
  const { categoryName } = params;
  const decodedCategoryName = decodeURIComponent(categoryName);

  const products = await getProducts();
  const filteredProducts = products.filter(p => p.category === decodedCategoryName);

  return (
    <div className="py-12">
      <div className="text-center">
        <h1 className="text-4xl font-bold text-gray-800">{decodedCategoryName}</h1>
        <p className="mt-2 text-lg text-gray-600">تصفح المنتجات المتوفرة في هذه الفئة</p>
      </div>

      {filteredProducts.length > 0 ? (
        <div className="mt-12 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
          {filteredProducts.map(product => (
            <div key={product.id} className="border rounded-lg overflow-hidden shadow-md hover:shadow-xl transition-shadow">
              <Link href={`/products/${product.id}`}>
                <div className="bg-gray-200 h-48 w-full flex items-center justify-center">
                  {/* Placeholder for Image */}
                  <span className="text-gray-500">صورة المنتج</span>
                </div>
                <div className="p-4 bg-white">
                  <h2 className="text-lg font-bold text-gray-800 truncate">{product.name}</h2>
                  <p className="text-sm text-gray-500">{product.model}</p>
                  <div className="mt-4 text-xl font-bold text-blue-600">
                    {typeof product.price === 'number' ? `${product.price} ر.س` : product.price}
                  </div>
                </div>
              </Link>
            </div>
          ))}
        </div>
      ) : (
        <div className="mt-12 text-center">
          <p className="text-xl text-gray-500">لا توجد منتجات في هذه الفئة حالياً.</p>
        </div>
      )}
    </div>
  );
}
