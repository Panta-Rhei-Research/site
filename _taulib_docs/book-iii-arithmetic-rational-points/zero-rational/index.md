---
{
  "projection_kind": "taulib_declaration",
  "title": "zero_rational",
  "permalink": "/corpus/taulib/docs/book-iii-arithmetic-rational-points/zero-rational/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.RationalPoints`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.RationalPoints::zero_rational",
  "declaration_slug": "zero-rational",
  "kind": "theorem",
  "name": "zero_rational",
  "module_name": "TauLib.BookIII.Arithmetic.RationalPoints",
  "module_url": "/corpus/taulib/docs/book-iii-arithmetic-rational-points/",
  "source_line_start": 176,
  "source_line_end": 177,
  "registry_ids": [
    "III.D59"
  ],
  "related_registry_items": [
    {
      "id": "III.D59",
      "title": "τ-Rational Point",
      "url": "/registry/object/III.D59/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L176-L177",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.RationalPoints",
        "url": "/corpus/taulib/docs/book-iii-arithmetic-rational-points/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L176-L177",
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

- Module: [TauLib.BookIII.Arithmetic.RationalPoints](/corpus/taulib/docs/book-iii-arithmetic-rational-points/)
- Source path: [`TauLib/BookIII/Arithmetic/RationalPoints.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/RationalPoints.lean#L176-L177)
- Source range: L176-L177
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `III.D59` — τ-Rational Point

## Immediate Comment / Docstring

```lean
/-- [III.D59] Structural: 0 is rational at every depth. -/
```

## Source Excerpt

```lean
theorem zero_rational :
    is_rational_at 0 3 = true := by native_decide
```
