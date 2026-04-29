---
{
  "projection_kind": "taulib_declaration",
  "title": "e3_predicate",
  "permalink": "/verify/taulib/docs/book-iii-mirror-e3-witness/e3-predicate/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Mirror.E3Witness`.",
  "declaration_id": "TauLib.BookIII.Mirror.E3Witness::e3_predicate",
  "declaration_slug": "e3-predicate",
  "kind": "def",
  "name": "e3_predicate",
  "module_name": "TauLib.BookIII.Mirror.E3Witness",
  "module_url": "/verify/taulib/docs/book-iii-mirror-e3-witness/",
  "source_line_start": 57,
  "source_line_end": 68,
  "registry_ids": [
    "III.D85"
  ],
  "related_registry_items": [
    {
      "id": "III.D85",
      "title": "Self-Referential Fixed Point",
      "url": "/registry/object/III.D85/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L57-L68",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Mirror.E3Witness",
        "url": "/verify/taulib/docs/book-iii-mirror-e3-witness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L57-L68",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
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

- Module: [TauLib.BookIII.Mirror.E3Witness](/verify/taulib/docs/book-iii-mirror-e3-witness/)
- Source path: [`TauLib/BookIII/Mirror/E3Witness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Mirror/E3Witness.lean#L57-L68)
- Source range: L57-L68
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D85` — Self-Referential Fixed Point

## Immediate Comment / Docstring

```lean
/-- [III.D85] E₃ predicate at stage k: triple-reduce stability and
    squaring compatibility. -/
```

## Source Excerpt

```lean
def e3_predicate (x k : Nat) : Bool :=
  let pk := primorial k
  if pk == 0 then true
  else
    let r1 := reduce x k
    let r2 := reduce r1 k
    let r3 := reduce r2 k
    -- Triple-reduce stable
    let triple_ok := r3 == r1
    -- Squaring compatible: reduce(x², k) = (reduce(x, k))² mod M_k
    let sq_ok := reduce (x * x) k == (r1 * r1) % pk
    triple_ok && sq_ok
```
