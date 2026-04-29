---
{
  "projection_kind": "taulib_declaration",
  "title": "IsRootOfUnity",
  "permalink": "/verify/taulib/docs/book-i-boundary-cyclotomic/is-root-of-unity/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Cyclotomic`.",
  "declaration_id": "TauLib.BookI.Boundary.Cyclotomic::IsRootOfUnity",
  "declaration_slug": "is-root-of-unity",
  "kind": "def",
  "name": "IsRootOfUnity",
  "module_name": "TauLib.BookI.Boundary.Cyclotomic",
  "module_url": "/verify/taulib/docs/book-i-boundary-cyclotomic/",
  "source_line_start": 41,
  "source_line_end": 46,
  "registry_ids": [
    "I.D88"
  ],
  "related_registry_items": [
    {
      "id": "I.D88",
      "title": "Cyclotomic Fields",
      "url": "/registry/object/I.D88/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L41-L46",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Cyclotomic",
        "url": "/verify/taulib/docs/book-i-boundary-cyclotomic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L41-L46",
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

- Module: [TauLib.BookI.Boundary.Cyclotomic](/verify/taulib/docs/book-i-boundary-cyclotomic/)
- Source path: [`TauLib/BookI/Boundary/Cyclotomic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Cyclotomic.lean#L41-L46)
- Source range: L41-L46
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D88` — Cyclotomic Fields

## Immediate Comment / Docstring

```lean
/-- [I.D88] z is an nth root of unity modulo m: z^n ≡ 1 (mod m). -/
```

## Source Excerpt

```lean
def IsRootOfUnity (n : Nat) (z m : TauIdx) : Prop :=
  z ^ n % m = 1 % m

/-- IsRootOfUnity is decidable (Nat equality is decidable). -/
instance (n : Nat) (z m : TauIdx) : Decidable (IsRootOfUnity n z m) :=
  inferInstanceAs (Decidable (_ = _))
```
