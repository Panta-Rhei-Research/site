---
{
  "projection_kind": "taulib_declaration",
  "title": "trichotomy_decompose",
  "permalink": "/verify/taulib/docs/book-iii-spectral-trichotomy/trichotomy-decompose/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectral.Trichotomy`.",
  "declaration_id": "TauLib.BookIII.Spectral.Trichotomy::trichotomy_decompose",
  "declaration_slug": "trichotomy-decompose",
  "kind": "def",
  "name": "trichotomy_decompose",
  "module_name": "TauLib.BookIII.Spectral.Trichotomy",
  "module_url": "/verify/taulib/docs/book-iii-spectral-trichotomy/",
  "source_line_start": 41,
  "source_line_end": 55,
  "registry_ids": [
    "III.T14"
  ],
  "related_registry_items": [
    {
      "id": "III.T14",
      "title": "Spectral Trichotomy Lemma",
      "url": "/registry/object/III.T14/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L41-L55",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectral.Trichotomy",
        "url": "/verify/taulib/docs/book-iii-spectral-trichotomy/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L41-L55",
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

- Module: [TauLib.BookIII.Spectral.Trichotomy](/verify/taulib/docs/book-iii-spectral-trichotomy/)
- Source path: [`TauLib/BookIII/Spectral/Trichotomy.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectral/Trichotomy.lean#L41-L55)
- Source range: L41-L55
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T14` — Spectral Trichotomy Lemma

## Immediate Comment / Docstring

```lean
/-- [III.T14] Decompose a CRT residue tuple into B-supported,
    C-supported, and X-supported components.
    Uses label_direct to classify each prime. -/
```

## Source Excerpt

```lean
def trichotomy_decompose (residues : List TauIdx) (k : TauIdx) :
    (List TauIdx × List TauIdx × List TauIdx) :=
  go residues 0 k [] [] []
where
  go (res : List TauIdx) (i k : Nat) (b_acc c_acc x_acc : List TauIdx) :
      (List TauIdx × List TauIdx × List TauIdx) :=
    if i >= k then (b_acc, c_acc, x_acc)
    else
      let p := nth_prime (i + 1)
      let ri := res.getD i 0
      let label := label_direct p
      match label with
      | .B => go res (i + 1) k (b_acc ++ [ri]) (c_acc ++ [0]) (x_acc ++ [0])
      | .C => go res (i + 1) k (b_acc ++ [0]) (c_acc ++ [ri]) (x_acc ++ [0])
      | .X => go res (i + 1) k (b_acc ++ [0]) (c_acc ++ [0]) (x_acc ++ [ri])
```
