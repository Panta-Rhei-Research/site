---
{
  "projection_kind": "taulib_declaration",
  "title": "radical_primorial_4",
  "permalink": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/radical-primorial-4/",
  "summary_short": "`theorem` declaration in `TauLib.BookIII.Arithmetic.ABCConjecture`.",
  "declaration_id": "TauLib.BookIII.Arithmetic.ABCConjecture::radical_primorial_4",
  "declaration_slug": "radical-primorial-4",
  "kind": "theorem",
  "name": "radical_primorial_4",
  "module_name": "TauLib.BookIII.Arithmetic.ABCConjecture",
  "module_url": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/",
  "source_line_start": 201,
  "source_line_end": 202,
  "registry_ids": [
    "III.P41"
  ],
  "related_registry_items": [
    {
      "id": "III.P41",
      "title": "Radical-Primorial Identity",
      "url": "/registry/object/III.P41/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L201-L202",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Arithmetic.ABCConjecture",
        "url": "/verify/taulib/docs/book-iii-arithmetic-abcconjecture/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L201-L202",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookIII.Arithmetic.ABCConjecture](/verify/taulib/docs/book-iii-arithmetic-abcconjecture/)
- Source path: [`TauLib/BookIII/Arithmetic/ABCConjecture.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Arithmetic/ABCConjecture.lean#L201-L202)
- Source range: L201-L202
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `III.P41` — Radical-Primorial Identity

## Immediate Comment / Docstring

```lean
/-- [III.P41] Radical-primorial identity up to depth 4. -/
```

## Source Excerpt

```lean
theorem radical_primorial_4 :
    radical_primorial_check 4 = true := by native_decide
```
