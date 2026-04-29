---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_residues_match",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-arith/crt-residues-match/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationArith`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationArith::crt_residues_match",
  "declaration_slug": "crt-residues-match",
  "kind": "def",
  "name": "crt_residues_match",
  "module_name": "TauLib.BookIII.Bridge.TranslationArith",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-arith/",
  "source_line_start": 89,
  "source_line_end": 98,
  "registry_ids": [
    "III.D88"
  ],
  "related_registry_items": [
    {
      "id": "III.D88",
      "title": "CRT-Integer Correspondence",
      "url": "/registry/object/III.D88/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L89-L98",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationArith",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-arith/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L89-L98",
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

- Module: [TauLib.BookIII.Bridge.TranslationArith](/verify/taulib/docs/book-iii-bridge-translation-arith/)
- Source path: [`TauLib/BookIII/Bridge/TranslationArith.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationArith.lean#L89-L98)
- Source range: L89-L98
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D88` — CRT-Integer Correspondence

## Immediate Comment / Docstring

```lean
/-- [III.D88] CRT residue match check: does y have the same residues as x
    for primes p_1, ..., p_k? -/
```

## Source Excerpt

```lean
def crt_residues_match (x y k : Nat) : Bool :=
  go 1 (k + 1) x y
where
  go (i bound x y : Nat) : Bool :=
    if i >= bound then true
    else
      let p := nth_prime i
      let ok := p == 0 || x % p == y % p
      ok && go (i + 1) bound x y
  termination_by bound - i
```
