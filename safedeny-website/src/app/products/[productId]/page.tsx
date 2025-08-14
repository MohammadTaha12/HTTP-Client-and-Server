import { notFound } from 'next/navigation';
import Image from 'next/image';
import Link from 'next/link';
import { Product } from '@/types';

async function getProduct(id: string): Promise<Product | undefined> {
  const baseUrl = process.env.VERCEL_URL ? `https://${process.env.VERCEL_URL}` : 'http://localhost:3000';
  const res = await fetch(`${baseUrl}/api/products`, { cache: 'no-store' });
  if (!res.ok) {
    throw new Error('Failed to fetch products');
  }
  const products: Product[] = await res.json();
  return products.find(p => p.id === id);
}

interface ProductPageProps {
  params: {
    productId: string;
  };
}

export default async function ProductPage({ params }: ProductPageProps) {
  const product = await getProduct(params.productId);

  if (!product) {
    notFound(); // This will render the not-found.tsx file or a default 404 page
  }

  return (
    <div className="py-12 bg-white">
      <div className="grid md:grid-cols-2 gap-8 lg:gap-12">
        {/* Image Gallery */}
        <div className="p-4 border rounded-lg">
           <div className="bg-gray-200 h-96 w-full flex items-center justify-center rounded-lg">
              {/* Placeholder for Image */}
              <span className="text-gray-500">صورة المنتج الرئيسية</span>
            </div>
          {/* Thumbnails could go here */}
        </div>

        {/* Product Info */}
        <div>
          <p className="text-sm text-gray-500">{product.brand} / {product.category}</p>
          <h1 className="text-3xl md:text-4xl font-bold text-gray-800 mt-2">{product.name}</h1>
          <p className="text-gray-600 mt-1">Model: {product.model}</p>

          <div className="mt-6 text-3xl font-bold text-blue-600">
            {typeof product.price === 'number' ? `${product.price} ر.س` : product.price}
          </div>

          {/* Action Button */}
          {typeof product.price !== 'number' && (
            <Link href="/contact" className="mt-6 inline-block w-full text-center bg-blue-600 text-white font-bold py-3 px-8 rounded-lg hover:bg-blue-700 transition-colors">
              اطلب عرض سعر
            </Link>
          )}

          <div className="mt-8">
            <h2 className="text-2xl font-bold border-b pb-2">الوصف والمواصفات</h2>
            <p className="mt-4 text-gray-700 whitespace-pre-wrap">{product.long_description}</p>
          </div>

          <div className="mt-8">
            <h2 className="text-2xl font-bold border-b pb-2">المستندات الفنية</h2>
            <ul className="mt-4 space-y-2">
              {product.docs.map(doc => (
                <li key={doc.name}>
                  <a href={doc.url} target="_blank" rel="noopener noreferrer" className="text-blue-600 hover:underline">
                    تحميل {doc.name}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
