---
{
  "projection_kind": "taulib_declaration",
  "title": "prime_polarity_scaling_check",
  "permalink": "/verify/taulib/docs/book-iii-doors-grand-grh/prime-polarity-scaling-check/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Doors.GrandGRH`.",
  "declaration_id": "TauLib.BookIII.Doors.GrandGRH::prime_polarity_scaling_check",
  "declaration_slug": "prime-polarity-scaling-check",
  "kind": "def",
  "name": "prime_polarity_scaling_check",
  "module_name": "TauLib.BookIII.Doors.GrandGRH",
  "module_url": "/verify/taulib/docs/book-iii-doors-grand-grh/",
  "source_line_start": 135,
  "source_line_end": 158,
  "registry_ids": [
    "III.T20"
  ],
  "related_registry_items": [
    {
      "id": "III.T20",
      "title": "Prime Polarity Scaling Theorem",
      "url": "/registry/object/III.T20/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L135-L158",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Doors.GrandGRH",
        "url": "/verify/taulib/docs/book-iii-doors-grand-grh/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L135-L158",
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

- Module: [TauLib.BookIII.Doors.GrandGRH](/verify/taulib/docs/book-iii-doors-grand-grh/)
- Source path: [`TauLib/BookIII/Doors/GrandGRH.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Doors/GrandGRH.lean#L135-L158)
- Source range: L135-L158
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.T20` — Prime Polarity Scaling Theorem

## Immediate Comment / Docstring

```lean
/-- [III.T20] Prime polarity scaling: the GRH decomposition into B/C/X
    sectors is compatible across primorial levels. Scaling from level k
    to k+1 preserves polarity type of each prime. -/
```

## Source Excerpt

```lean
def prime_polarity_scaling_check (db : TauIdx) : Bool :=
  go 1 1 ((db + 1) * (db + 1))
where
  go (i k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if k >= db then true
    else if i > k then
      -- All primes at depth k checked; verify product extension
      let b_k := split_zeta_b k
      let b_k1 := split_zeta_b (k + 1)
      let b_extends := if b_k > 0 then b_k1 % b_k == 0 else true
      let c_k := split_zeta_c k
      let c_k1 := split_zeta_c (k + 1)
      let c_extends := if c_k > 0 then c_k1 % c_k == 0 else true
      b_extends && c_extends && go 1 (k + 1) (fuel - 1)
    else
      -- Verify label classification against mod-4 residue (not self-comparison)
      let p := nth_prime i
      let label := label_direct p
      let mod4_ok := if p % 4 == 1 then label == .B
                     else if p % 4 == 3 then label == .C
                     else true
      mod4_ok && go (i + 1) k (fuel - 1)
  termination_by fuel
```
