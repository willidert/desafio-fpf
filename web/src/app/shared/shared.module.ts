import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { SearchFilterPipe } from './pipes/search-filter.pipe';

@NgModule({
  declarations: [SearchFilterPipe],
  imports: [CommonModule],
  exports: [SearchFilterPipe],
})
export class SharedModule {}
