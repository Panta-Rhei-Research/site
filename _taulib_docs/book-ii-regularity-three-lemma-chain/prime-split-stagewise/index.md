---
{
  "projection_kind": "taulib_declaration",
  "title": "prime_split_stagewise",
  "permalink": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/prime-split-stagewise/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.ThreeLemmaChain`.",
  "declaration_id": "TauLib.BookII.Regularity.ThreeLemmaChain::prime_split_stagewise",
  "declaration_slug": "prime-split-stagewise",
  "kind": "def",
  "name": "prime_split_stagewise",
  "module_name": "TauLib.BookII.Regularity.ThreeLemmaChain",
  "module_url": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/",
  "source_line_start": 141,
  "source_line_end": 156,
  "registry_ids": [
    "II.L09"
  ],
  "related_registry_items": [
    {
      "id": "II.L09",
      "title": "Prime-Split Support",
      "url": "/registry/object/II.L09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L141-L156",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.ThreeLemmaChain",
        "url": "/verify/taulib/docs/book-ii-regularity-three-lemma-chain/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L141-L156",
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

- Module: [TauLib.BookII.Regularity.ThreeLemmaChain](/verify/taulib/docs/book-ii-regularity-three-lemma-chain/)
- Source path: [`TauLib/BookII/Regularity/ThreeLemmaChain.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/ThreeLemmaChain.lean#L141-L156)
- Source range: L141-L156
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.L09` — Prime-Split Support

## Immediate Comment / Docstring

```lean
/-- [II.L09] Stage-level prime-split: at each primorial stage k,
    the B-channel and C-channel of the reduced value maintain
    disjoint support after reduction. -/
```

## Source Excerpt

```lean
def prime_split_stagewise (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      let rx := reduce x k
      let p := from_tau_idx rx
      let bp := interior_bipolar p
      let (g_plus, g_minus) := idempotent_decompose bp
      -- Disjoint support at this stage
      let ok := g_plus.c_sector == 0 && g_minus.b_sector == 0
      ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```
