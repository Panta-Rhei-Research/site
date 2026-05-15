---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRat.mul_inv_cancel",
  "permalink": "/corpus/taulib/docs/book-i-boundary-tau-rat-inv/mul-inv-cancel/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.TauRatInv`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRatInv::TauRat.mul_inv_cancel",
  "declaration_slug": "mul-inv-cancel",
  "kind": "theorem",
  "name": "TauRat.mul_inv_cancel",
  "module_name": "TauLib.BookI.Boundary.TauRatInv",
  "module_url": "/corpus/taulib/docs/book-i-boundary-tau-rat-inv/",
  "source_line_start": 152,
  "source_line_end": 156,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L152-L156",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRatInv",
        "url": "/corpus/taulib/docs/book-i-boundary-tau-rat-inv/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L152-L156",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.Boundary.TauRatInv](/corpus/taulib/docs/book-i-boundary-tau-rat-inv/)
- Source path: [`TauLib/BookI/Boundary/TauRatInv.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRatInv.lean#L152-L156)
- Source range: L152-L156
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `q · q⁻¹ ≡ 1` up to `TauRat.equiv`, assuming `q` is nonzero. -/
```

## Source Excerpt

```lean
theorem TauRat.mul_inv_cancel (q : TauRat) (h : q.is_nonzero) :
    TauRat.equiv (q.mul (q.inv h)) TauRat.one := by
  rw [equiv_iff_toRat_eq, toRat_mul, toRat_inv, toRat_one]
  rw [(TauRat.is_nonzero_iff_toRat_ne_zero q).mp h
      |> mul_inv_cancel₀]
```
