---
{
  "projection_kind": "taulib_declaration",
  "title": "cylinder_gen",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/cylinder-gen/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CanonicalBasis`.",
  "declaration_id": "TauLib.BookII.Hartogs.CanonicalBasis::cylinder_gen",
  "declaration_slug": "cylinder-gen",
  "kind": "def",
  "name": "cylinder_gen",
  "module_name": "TauLib.BookII.Hartogs.CanonicalBasis",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/",
  "source_line_start": 52,
  "source_line_end": 56,
  "registry_ids": [
    "II.D46"
  ],
  "related_registry_items": [
    {
      "id": "II.D46",
      "title": "Cylinder Generator",
      "url": "/registry/object/II.D46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L52-L56",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CanonicalBasis",
        "url": "/verify/taulib/docs/book-ii-hartogs-canonical-basis/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L52-L56",
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

- Module: [TauLib.BookII.Hartogs.CanonicalBasis](/verify/taulib/docs/book-ii-hartogs-canonical-basis/)
- Source path: [`TauLib/BookII/Hartogs/CanonicalBasis.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CanonicalBasis.lean#L52-L56)
- Source range: L52-L56
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D46` — Cylinder Generator

## Immediate Comment / Docstring

```lean
/-- [II.D46] Cylinder generator E_{k,prime_idx,v}^(sigma)(x).

    Returns 1 if x (reduced to stage k) falls in residue class v
    modulo the prime p_{prime_idx}, and 0 otherwise. -/
```

## Source Excerpt

```lean
def cylinder_gen (k prime_idx v : TauIdx) (_sigma : Bool) (x : TauIdx) : Int :=
  let rx := reduce x k
  let p := nth_prime prime_idx
  if p == 0 then 0
  else if rx % p == v then 1 else 0
```
